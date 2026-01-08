
import pytest
from elysia_engine.hypersphere import (
    CelestialHierarchy,
    TesseractCoord,
    HypersphereMemory,
    SoulProtocol,
    MemoryPattern,
    TesseractVault
)
from elysia_engine.tensor import SoulTensor

def test_celestial_hierarchy():
    """Test that the 7 Angels/Demons mapping is correct."""
    # Test Angels (Positive)
    assert "Angel Rank 7" in CelestialHierarchy.analyze_frequency(7.0)
    assert "Angel Rank 1" in CelestialHierarchy.analyze_frequency(1.0)
    assert "High Frequency" in CelestialHierarchy.analyze_frequency(5.0)

    # Test Demons (Negative)
    assert "Demon Rank 7" in CelestialHierarchy.analyze_frequency(-7.0)
    assert "Demon Rank 1" in CelestialHierarchy.analyze_frequency(-1.0)
    assert "Low Frequency" in CelestialHierarchy.analyze_frequency(-5.0)

    # Test Neutral
    assert "Human/Void" in CelestialHierarchy.analyze_frequency(0.0)

def test_tesseract_coord_conversion():
    """Test that Tesseract coordinates convert to Quaternions correctly."""
    coord = TesseractCoord(w=1.0, x=0.5, y=7.0, z=-1.0)
    quat = coord.to_quaternion()

    assert quat.w == 1.0
    assert quat.x == 0.5
    assert quat.y == 7.0
    assert quat.z == -1.0

def test_soul_protocol():
    """Test the Tesseract-Soul Protocol helper functions."""
    # Boundary Check
    assert SoulProtocol.boundary_check(5.0) == 5.0
    assert SoulProtocol.boundary_check(-1.0) == 0.0 # Clamping

    # Frequency Scan
    assert SoulProtocol.frequency_scan(1.0) == 7.0 # +1.0 sentiment -> +7 Angel
    assert SoulProtocol.frequency_scan(-1.0) == -7.0 # -1.0 sentiment -> -7 Demon

    # Trajectory
    z, x = SoulProtocol.map_trajectory(1.0, 0.5)
    assert z == 1.0
    assert x == 0.5

def test_hypersphere_fractal_storage():
    """Test storing a Hypersphere inside another Hypersphere (Fractal)."""
    # Create the Inner Universe (Microcosm)
    inner_memory = HypersphereMemory()
    inner_soul = SoulTensor(amplitude=1.0, frequency=7.0, phase=0.0)
    inner_coord = TesseractCoord(w=0, x=0, y=7, z=0)
    inner_memory.store("Angel Core", inner_coord, inner_soul)

    # Create the Outer Universe (Macrocosm)
    outer_memory = HypersphereMemory()
    outer_soul = SoulTensor(amplitude=10.0, frequency=0.0, phase=0.0)
    outer_coord = TesseractCoord(w=10, x=0, y=0, z=0)

    # Store the Inner Universe into the Outer
    pattern = outer_memory.store(
        content=inner_memory,
        coord=outer_coord,
        soul_tensor=outer_soul,
        topology="Fractal",
        name="Inner Heaven"
    )

    # Retrieve and verify
    retrieved = outer_memory.query(outer_coord, radius=0.1)[0]
    assert isinstance(retrieved.content, HypersphereMemory)
    assert retrieved.content.patterns[0][1].content == "Angel Core"
    assert "Fractal" in retrieved.summary

def test_tesseract_vault_safety():
    """Test the safety limits of the Tesseract Vault."""

    # 1. Test Entropy Analysis
    memory = HypersphereMemory()
    memory.store("Angel", TesseractCoord(0,0,0,0), SoulTensor(1, 7, 0)) # +7
    memory.store("Demon", TesseractCoord(0,0,0,0), SoulTensor(1, -7, 0)) # -7
    # Balanced (7 vs 7) -> 50% ratio
    assert "Stable" in TesseractVault.analyze_entropy(memory)

    memory_chaos = HypersphereMemory()
    memory_chaos.store("Demon", TesseractCoord(0,0,0,0), SoulTensor(1, -7, 0))
    # All negative -> Ratio 0
    assert "Abyss Collapse" in TesseractVault.analyze_entropy(memory_chaos)

    # 2. Test Max Fractal Depth
    # Depth 0 (Main) -> Depth 1 (L1) -> Depth 2 (L2) -> Depth 3 (L3) -> Depth 4 (Overflow)

    # Create layers
    l3 = HypersphereMemory()
    l2 = HypersphereMemory()
    l1 = HypersphereMemory()
    main = HypersphereMemory()

    # Build from bottom up
    # Note: store() doesn't recursively check *during* storage object creation,
    # it checks when we try to put a universe into another.

    # We need to simulate the recursion check directly or via store

    # This should pass (Depth 0 storing Depth 1)
    l2.store("Content", TesseractCoord(0,0,0,0), SoulTensor(1,1,1))
    l1.store(l2, TesseractCoord(0,0,0,0), SoulTensor(1,1,1))

    # Checking depth manually for clarity of test
    # l1 contains l2. l1 is at depth 1.
    assert TesseractVault.check_fractal_depth(l1, current_depth=1) == True

    # Construct a chain that is too deep
    # Root -> L1 -> L2 -> L3 -> L4 (Too Deep)

    # Create independent universes (depth is initially 0 for all)
    l4 = HypersphereMemory()
    l3 = HypersphereMemory()
    l2_deep = HypersphereMemory()
    l1_deep = HypersphereMemory()
    main = HypersphereMemory()

    # Link them bottom-up.
    # Store updates depth of the child.

    l3.store(l4, TesseractCoord(0,0,0,0), SoulTensor(1,1,1))
    # l3 is depth 0. l4 becomes depth 1 (relative to l3? No, l4 is depth 1 inside l3).
    # Wait, l3 is standalone, depth=0. Inside l3, l4 is at l3.depth+1 = 1.

    l2_deep.store(l3, TesseractCoord(0,0,0,0), SoulTensor(1,1,1))
    # l2 is depth 0. l3 becomes depth 1. l4 becomes depth 2.

    l1_deep.store(l2_deep, TesseractCoord(0,0,0,0), SoulTensor(1,1,1))
    # l1 is depth 0. l2 becomes depth 1. l3 becomes depth 2. l4 becomes depth 3.

    # Now try to store l1_deep into main.
    # Main is depth 0. l1 will become depth 1.
    # l2 -> 2. l3 -> 3. l4 -> 4.
    # Max depth is 3. So l4 at depth 4 should fail.

    with pytest.raises(OverflowError):
        main.store(l1_deep, TesseractCoord(0,0,0,0), SoulTensor(1,1,1))
