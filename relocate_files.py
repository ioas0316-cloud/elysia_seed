import os
import shutil

moves = [
    # Core L0 -> L1 M1
    (r"c:\Elysia\Core\L0_Keystone\sovereignty_wave.py", r"c:\Elysia\Core\L1_Foundation\M1_Keystone\sovereignty_wave.py"),
    (r"c:\Elysia\Core\L0_Keystone\field_phonetics.py", r"c:\Elysia\Core\L1_Foundation\M1_Keystone\field_phonetics.py"),
    (r"c:\Elysia\Core\L0_Keystone\hunminjeongeum.py", r"c:\Elysia\Core\L1_Foundation\M1_Keystone\hunminjeongeum.py"),
    (r"c:\Elysia\Core\L0_Keystone\monadic_lexicon.py", r"c:\Elysia\Core\L1_Foundation\M1_Keystone\monadic_lexicon.py"),
    (r"c:\Elysia\Core\L0_Keystone\syllable_composer.py", r"c:\Elysia\Core\L1_Foundation\M1_Keystone\syllable_composer.py"),
    
    # Docs L0 -> L1 M1
    (r"c:\Elysia\docs\L0_Keystone\CODEX_SOVEREIGN.md", r"c:\Elysia\docs\L1_Foundation\M1_Keystone\CODEX_SOVEREIGN.md"),
    (r"c:\Elysia\docs\L0_Keystone\FAQ.md", r"c:\Elysia\docs\L1_Foundation\M1_Keystone\FAQ.md"),
    (r"c:\Elysia\docs\L0_Keystone\QUICKSTART.md", r"c:\Elysia\docs\L1_Foundation\M1_Keystone\QUICKSTART.md"),
    
    # Core L6 Merkaba -> L6 M1
    (r"c:\Elysia\Core\L6_Structure\Merkaba\dimensional_error_diagnosis.py", r"c:\Elysia\Core\L6_Structure\M1_Merkaba\dimensional_error_diagnosis.py"),
    (r"c:\Elysia\Core\L6_Structure\Merkaba\hypersphere_field.py", r"c:\Elysia\Core\L6_Structure\M1_Merkaba\hypersphere_field.py"),
    
    # Core Experience -> L7 M4
    (r"c:\Elysia\Core\L5_Mental\Intelligence\Sovereign\experience_cortex.py", r"c:\Elysia\Core\L7_Spirit\M4_Experience\experience_cortex.py"),
    
    # Docs Spirit Genesis -> L7 M5
    (r"c:\Elysia\docs\L7_Spirit\M5_Genesis\GENESIS_ORIGIN.md", r"c:\Elysia\docs\L7_Spirit\M5_Genesis\GENESIS_ORIGIN.md"), # Already there but good to be explicit
]

for src, dst in moves:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        print(f"Moved: {src} -> {dst}")
    else:
        print(f"Source not found: {src}")
