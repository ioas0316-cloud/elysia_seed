"""
Sovereign Observer (The Eye of the World)
=========================================
Core.Eye.sovereign_observer

"To create a World, one must first observe a World."

Adapted for Elysia Seed: Robust Mobile/Desktop Hybrid.
Retains full visual capture capabilities if libraries permit.
"""

import psutil
import time
import logging
import os
import threading
from typing import Optional

# Try to import ImageGrab for visual capture
try:
    from PIL import ImageGrab
    HAS_VISION = True
except ImportError:
    HAS_VISION = False

logger = logging.getLogger("SovereignObserver")

class SovereignObserver:
    def __init__(self, target_process_name: str = "Wuthering Waves.exe"):
        self.target_name = target_process_name
        self.target_candidates = [
            target_process_name,
            "Client-Win64-Shipping.exe", 
            "Wuthering Waves.exe",
            "launcher.exe",
            "com.kurogame.mingchao" # Android Package Name Example
        ]
        self.target_pid: Optional[int] = None
        self.process: Optional[psutil.Process] = None
        self.is_observing = False
        self.vision_memory_path = "Memories/Visual/Observer"
        
        os.makedirs(self.vision_memory_path, exist_ok=True)
        logger.info(f"👁️ [Observer] Initialized. Hunting for world: {self.target_name}")

    def scan_for_target(self) -> bool:
        """Scans the process list for the target world."""
        # On Android (Termux), psutil might have limited access, 
        # but we keep this logic for cross-platform robustness.
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                proc_name = proc.info['name']
                for candidate in self.target_candidates:
                    if candidate.lower() in proc_name.lower():
                        self.target_pid = proc.info['pid']
                        self.process = psutil.Process(self.target_pid)
                        self.target_name = proc_name
                        logger.info(f"🎯 [Target Locked] Found {proc_name} (PID: {self.target_pid})")
                        return True
            except: pass
        return False

    def start_observation(self):
        """Begins the loop of Structural and Visual analysis."""
        if not self.target_pid and not self.scan_for_target():
            logger.warning("⚠️ [Observer] Target world not found. Entering Passive Mode.")
            # We don't return here; we enter a passive wait loop in the thread
        
        self.is_observing = True
        threading.Thread(target=self._observation_loop, daemon=True).start()
        logger.info("🔭 [Observer] Observation Uplink Established.")

    def _observation_loop(self):
        snapshot_interval = 30
        last_snapshot = 0
        
        while self.is_observing:
            try:
                # 1. Re-scan if lost
                if not self.process or not self.process.is_running():
                    if self.scan_for_target():
                        logger.info("🎯 [Observer] Re-acquired Target.")
                    else:
                        time.sleep(5)
                        continue

                # 2. Process Telemetry
                cpu = self.process.cpu_percent(interval=0.1)
                mem = self.process.memory_info().rss / (1024 * 1024)
                
                world_state = "Stable"
                if cpu > 50: world_state = "High_Dynamics"
                
                # 3. Visual Observation
                now = time.time()
                if HAS_VISION and (now - last_snapshot > snapshot_interval):
                    self._capture_visual_qualia(world_state)
                    last_snapshot = now
                
                time.sleep(5)

            except Exception as e:
                logger.error(f"❌ [Observer] Glitch: {e}")
                time.sleep(1)

    def _capture_visual_qualia(self, context_tag: str):
        try:
            screenshot = ImageGrab.grab()
            timestamp = int(time.time())
            filename = f"seed_vision_{timestamp}.png"
            path = os.path.join(self.vision_memory_path, filename)
            
            # Resize for mobile efficiency (Seed Optimization)
            screenshot = screenshot.resize((512, 512)) 
            screenshot.save(path)
            
            logger.info(f"📸 [Vision] Captured World Fragment: {filename}")
            
        except Exception as e:
            logger.error(f"❌ [Vision] Capture Failed: {e}")

    def stop(self):
        self.is_observing = False
        logger.info("🛑 [Observer] Link Severed.")
