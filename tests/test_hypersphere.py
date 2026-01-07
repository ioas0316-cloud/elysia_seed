import math
import pytest
from elysia_engine.math_utils import Quaternion
from elysia_engine.tensor import SoulTensor
from elysia_engine.hypersphere import (
    HypersphericalCoord,
    HypersphereMemory,
    PsychologyMapper,
    MemoryPattern
)

def test_hyperspherical_coord_to_quaternion():
    # Test origin
    c = HypersphericalCoord(0, 0, 0, 0)
    q = c.to_quaternion()
    assert q.w == 0 and q.x == 0 and q.y == 0 and q.z == 0

    # Test unit quaternion along w axis (Identity rotation)
    # w = r * cos(t3). If t3=0, w=r. x,y,z depend on sin(t3)=0 -> 0.
    c = HypersphericalCoord(0, 0, 0, 1.0)
    q = c.to_quaternion()
    assert abs(q.w - 1.0) < 1e-6
    assert abs(q.x) < 1e-6

def test_distance_angular():
    # c1: t3=0 -> w=1 (Identity)
    c1 = HypersphericalCoord(0, 0, 0, 1.0)

    # c2: t3=pi/2 -> w=0. z=1*1*cos(0)=1. x,y=0.
    # So c2 is (w=0, z=1, y=0, x=0) -> 90 degree rotation around z-axis?
    # q2 = (0, 0, 0, 1) or similar.
    c2 = HypersphericalCoord(0, 0, math.pi/2, 1.0)

    q1 = c1.to_quaternion()
    q2 = c2.to_quaternion()

    # Dot product: (1*0 + 0*0 + 0*0 + 0*1) = 0
    # acos(0) = pi/2

    dist = c1.distance_to(c2)
    assert abs(dist - math.pi/2) < 1e-6

    # c3: t3=pi -> w=-1. x,y,z=0.
    c3 = HypersphericalCoord(0, 0, math.pi, 1.0)
    # Dot product: 1*-1 = -1
    # acos(-1) = pi
    dist_pi = c1.distance_to(c3)
    assert abs(dist_pi - math.pi) < 1e-6

def test_distance_angular_with_depth():
    # Test identical points with r=0.5 (Depth != 1)
    c1 = HypersphericalCoord(0, 0, 0, 0.5)
    c2 = HypersphericalCoord(0, 0, 0, 0.5)

    # Distance should be 0 (same angle)
    dist = c1.distance_to(c2)
    assert abs(dist) < 1e-6

    # Test orthogonal points with r=2.0
    c3 = HypersphericalCoord(0, 0, 0, 2.0)      # w axis
    c4 = HypersphericalCoord(0, 0, math.pi/2, 2.0) # z axis

    dist_ortho = c3.distance_to(c4)
    assert abs(dist_ortho - math.pi/2) < 1e-6

def test_psychology_mapper():
    # Joy (+1) -> theta2 = 0
    # Analytic (+1) -> theta1 = 0
    # Active (+1) -> theta3 = 0
    c = PsychologyMapper.map_intent(1.0, 1.0, 1.0, 1.0)
    assert c.theta1 == 0.0
    assert c.theta2 == 0.0
    assert c.theta3 == 0.0
    assert c.r == 1.0

    # Sad (-1) -> theta2 = pi
    c_sad = PsychologyMapper.map_intent(1.0, -1.0, 1.0, 1.0)
    assert abs(c_sad.theta2 - math.pi) < 1e-6

def test_memory_store_and_query():
    mem = HypersphereMemory()

    # Create a "Joy" coordinate
    joy_coord = PsychologyMapper.map_intent(0, 1.0, 0, 1.0)

    # Create a SoulTensor
    st = SoulTensor(amplitude=10, frequency=440, phase=0)

    # Store
    mem.store("Happy Memory", joy_coord, st, name="FirstKiss")

    # Query exact location
    results = mem.query(joy_coord, radius=0.1)
    assert len(results) == 1
    assert results[0].content == "Happy Memory"
    assert results[0].name == "FirstKiss"

    # Query far away (Sad coordinate)
    sad_coord = PsychologyMapper.map_intent(0, -1.0, 0, 1.0)
    results_sad = mem.query(sad_coord, radius=0.1)
    assert len(results_sad) == 0

def test_resonance_scanner():
    mem = HypersphereMemory()

    # Store 3 memories with different frequencies
    st1 = SoulTensor(amplitude=1, frequency=100, phase=0) # Low
    st2 = SoulTensor(amplitude=1, frequency=500, phase=0) # Mid
    st3 = SoulTensor(amplitude=1, frequency=1000, phase=0) # High

    coord = HypersphericalCoord(0,0,0,1)

    mem.store("LowFreq", coord, st1)
    mem.store("MidFreq", coord, st2)
    mem.store("HighFreq", coord, st3)

    # Scan for Mid range (400-600)
    results = mem.scan(frequency_range=(400, 600))
    assert len(results) == 1
    assert results[0].content == "MidFreq"

    # Scan for High range
    results_high = mem.scan(frequency_range=(900, 1100))
    assert len(results_high) == 1
    assert results_high[0].content == "HighFreq"

def test_master_map():
    mem = HypersphereMemory()

    # Add a named memory
    coord = HypersphericalCoord(0,0,0,1) # Joy/Analytic/Active sector approx
    st = SoulTensor(amplitude=1, frequency=100, phase=0)
    mem.store("NamedMem", coord, st, name="Landmark1")

    # Add unnamed memory in specific sector
    # Logic=High (0..pi), Emotion=Neg (pi..2pi? No, 0..2pi. wait. Mapper maps -1..1 to pi..0)
    # So Sad is pi.
    sad_coord = HypersphericalCoord(0, math.pi, 0, 1) # Logic High, Emotion Neg
    mem.store("SadMem", sad_coord, st)

    m_map = mem.get_master_map()

    assert m_map["total_memories"] == 2
    assert "Landmark1" in m_map["sovereign_locations"]

    # Check sectors
    # coord (0,0,0) -> Logic High (0 < pi), Emotion Pos (0 < pi)
    # sad_coord (0, pi, 0) -> Logic High, Emotion Neg (pi >= pi? No, range is 0..2pi? )
    # Let's check logic in _analyze_sectors:
    # if 0 <= coord.theta2 < math.pi: sectors["Emotion_Pos"] += 1
    # else: sectors["Emotion_Neg"] += 1

    # Joy (0) -> Pos
    # Sad (pi) -> Neg (pi is not < pi)

    assert m_map["sectors"]["Emotion_Pos"] >= 1
    assert m_map["sectors"]["Emotion_Neg"] >= 1

def test_resonance_query():
    mem = HypersphereMemory()
    coord = HypersphericalCoord(0, 0, 0, 1)

    # Create a probe soul
    probe = SoulTensor(amplitude=1, frequency=100, phase=0)

    # 1. Perfect Match (Phase diff 0 -> Res 1.0)
    st_match = SoulTensor(amplitude=1, frequency=100, phase=0)
    mem.store("Match", coord, st_match)

    # 2. Opposite Phase (Phase diff pi -> Res -1.0)
    st_opp = SoulTensor(amplitude=1, frequency=100, phase=math.pi)
    mem.store("Opposite", coord, st_opp)

    # 3. Orthogonal Phase (Phase diff pi/2 -> Res 0.0)
    st_ortho = SoulTensor(amplitude=1, frequency=100, phase=math.pi/2)
    mem.store("Orthogonal", coord, st_ortho)

    # Query with high threshold (e.g., > 0.7)
    results = mem.resonance_query(coord, probe, resonance_threshold=0.7)

    # Should only find the Match
    assert len(results) == 1
    assert results[0].content == "Match"

    # Query with negative threshold to find everything better than "Opposite"
    # -1.0 is lowest possible.
    results_all = mem.resonance_query(coord, probe, resonance_threshold=-0.9)
    # Should find Match(1.0) and Ortho(0.0). Opposite is -1.0, so maybe excluded if strict >?
    # Logic is >= threshold. -1.0 >= -0.9 is False. So Opposite is excluded.
    # Match (1.0) included. Ortho (0.0) included.
    assert len(results_all) == 2
