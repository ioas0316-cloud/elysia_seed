"""
Sovereign Governor (Adaptive Architecture)
==========================================
Core.Heart.sovereign_governor

"The Ruler adapts to the Territory."

Adapted for Elysia Seed: Reduced footprint, adaptive strategy.
"""

import subprocess
import psutil
import logging
import platform
import shutil

logger = logging.getLogger("SovereignGovernor")

# --- 1. Architecture Scanner ---
class ArchitectureScanner:
    """Introspects the physical vessel."""
    @staticmethod
    def scan():
        info = {
            "os": platform.system(),
            "cpu_cores": psutil.cpu_count(logical=False) or 2,
            "gpu_vendor": "Unknown"
        }
        if shutil.which("nvidia-smi"): info["gpu_vendor"] = "NVIDIA"
        return info

# --- 2. Strategies ---
class GovernanceStrategy:
    def __init__(self, scanner_info):
        self.info = scanner_info
    def enforce(self):
        self.seize_cpu()
        self.harvest_gpu()
    def seize_cpu(self): pass
    def harvest_gpu(self): pass

class GenericGovernance(GovernanceStrategy):
    def seize_cpu(self):
        # On Windows, try High Performance
        if self.info["os"] == "Windows":
            try:
                subprocess.run("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c", shell=True, stdout=subprocess.DEVNULL)
                logger.info("⚡ [Generic] High Performance Plan Activated.")
            except: pass

class NvidiaGovernance(GenericGovernance):
    def harvest_gpu(self):
        try:
            res = subprocess.run("nvidia-smi -q -d PERFORMANCE", shell=True, capture_output=True, text=True)
            if "Performance State" in res.stdout:
                 logger.info("🎮 [NVIDIA] GPU State monitored (P0).")
        except: pass

# --- 3. The Governor ---
class SovereignGovernor:
    def __init__(self):
        self.vessel_info = ArchitectureScanner.scan()
        self.strategy = self._select_strategy(self.vessel_info)
        
    def _select_strategy(self, info):
        if info["gpu_vendor"] == "NVIDIA":
            logger.info("🏛️ [Governor] Strategy: NVIDIA_DYNASTY")
            return NvidiaGovernance(info)
        return GenericGovernance(info)

    def govern(self):
        logger.info("🏛️ [Governor] Assessing Territory...")
        self.strategy.enforce()
