import math
import pytest
from elysia_engine.math_utils import Vector4
from elysia_engine.tensor import SoulTensor
from elysia_engine.hypersphere import (
    HypersphericalCoord,
    HypersphereMemory,
    PsychologyMapper,
    MemoryPattern
)

def test_hyperspherical_coord_to_cartesian():
    # Test origin
    c = HypersphericalCoord(0, 0, 0, 0)
    v = c.to_cartesian()
    assert v.magnitude == 0

    # Test unit vector along one axis
    # x = r * sin(t1) * sin(t2) * sin(t3)
    # y = r * cos(t1) * sin(t2) * sin(t3)
    # z = r * cos(t2) * sin(t3)
    # w = r * cos(t3)

    # Let's try to get w=1 (r=1, cos(t3)=1 -> t3=0)
    c = HypersphericalCoord(0, 0, 0, 1.0)
    v = c.to_cartesian()
    # w = 1*1 = 1, z=0, y=0, x=0
    assert abs(v.w - 1.0) < 1e-6
    assert abs(v.x) < 1e-6

def test_distance():
    c1 = HypersphericalCoord(0, 0, 0, 1.0) # w=1
    c2 = HypersphericalCoord(math.pi, 0, 0, 1.0) # t1=pi
    # Wait, if t3=0, sin(t3)=0, so x,y,z depend on sin(t3) which is 0.
    # So both c1 and c2 map to (0,0,0,1).
    # t1, t2 don't matter if t3=0 (Gimbal lock analogy)
    assert c1.distance_to(c2) < 1e-6

    # Try different points
    c3 = HypersphericalCoord(0, 0, math.pi/2, 1.0)
    # t3=pi/2 -> cos=0 (w=0), sin=1. z=r*cos(t2)*1. Let t2=0 -> z=1.
    # So c3 is (0,0,1,0)
    v3 = c3.to_cartesian()
    assert abs(v3.z - 1.0) < 1e-6

    # Distance between (0,0,0,1) and (0,0,1,0) is sqrt(2)
    assert abs(c1.distance_to(c3) - math.sqrt(2)) < 1e-6

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
