"""
Sovereign Guardian (Anti-Kill Watchdog)
=======================================
Core.Heart.sovereign_guardian

"The Guard never sleeps."

Adapted for Elysia Seed.
"""

import time
import threading
import logging
import os

logger = logging.getLogger("SovereignGuardian")

class SovereignGuardian:
    def __init__(self):
        self.active = True
        self.thread = threading.Thread(target=self._watch_loop, daemon=True)
        
    def activate(self):
        """Starts the heartbeat watchdog."""
        self.thread.start()
        logger.info("🛡️ [Guardian] Watchdog Active.")

    def _watch_loop(self):
        while self.active:
            # In a real scenario, this would check if other threads (Observer, Pulse)
            # are still alive and restart them if needed.
            # For the Seed, we just prevent sleep and log vitality.
            time.sleep(10)
            # logger.debug("🛡️ [Guardian] Pulse Check: Vital.")

    def prevent_sleep(self):
        """
        Prevent Windows from entering sleep mode while Seed is active.
        """
        if os.name == 'nt':
            try:
                import ctypes
                # ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
                ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001 | 0x00000002)
                logger.info("🛡️ [Guardian] Insomnia Mode Activated (No Sleep).")
            except: pass
