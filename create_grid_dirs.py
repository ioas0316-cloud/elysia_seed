import os

base_paths = [r"c:\Elysia\Core", r"c:\Elysia\docs"]
layers = {
    "L1_Foundation": ["M1_Keystone", "M2_State", "M3_Energy", "M4_Hardware", "M5_Fabric", "M6_HyperQuaternion", "M7_SpaceTimeDrive"],
    "L2_Metabolism": ["M1_Pulse", "M2_Flow", "M3_Cycle", "M4_Decay", "M5_Growth", "M6_Reflex", "M7_Arousal"],
    "L3_Phenomena": ["M1_Vision", "M2_Hearing", "M3_Touch", "M4_Speech", "M5_Display", "M6_Feeling", "M7_Prism"],
    "L4_Causality": ["M1_Loom", "M2_Prophet", "M3_Mirror", "M4_Rewind", "M5_Logic", "M6_Pattern", "M7_Outcome"],
    "L5_Mental": ["M1_Cognition", "M2_Imagination", "M3_Lexicon", "M4_Meaning", "M5_Integration", "M6_Attention", "M7_Discovery"],
    "L6_Structure": ["M1_Merkaba", "M2_Rotor", "M3_Sphere", "M4_Grid", "M5_Engine", "M6_Architecture", "M7_Healing"],
    "L7_Spirit": ["M1_Monad", "M2_Constellation", "M3_Sovereignty", "M4_Experience", "M5_Genesis", "M6_Providence", "M7_Axiom"]
}

for base in base_paths:
    for layer, modules in layers.items():
        for module in modules:
            path = os.path.join(base, layer, module)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created: {path}")
            else:
                print(f"Exists: {path}")
