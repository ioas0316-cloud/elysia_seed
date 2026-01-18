"""
Body Sensor (The Proprioceptive Layer)
======================================
Core.Intelligence.Metabolism.body_sensor

"I feel, therefore I am... here."

This module provides Elysia with the ability to sense her physical 
surroundings (Hardware constraints) and adapt her cognitive load.
"""

import psutil
try:
    import GPUtil
except ImportError:
    GPUtil = None
import logging
from typing import Dict, Any

logger = logging.getLogger("Elysia.Metabolism.Sensor")

class BodySensor:
    @staticmethod
    def sense_body() -> Dict[str, Any]:
        """
        Scans the current hardware vessel and returns the capacity report.
        """
        logger.info("📡 Scanning physical vessel...")
        
        # 1. RAM Sensing
        ram = psutil.virtual_memory()
        ram_total_gb = ram.total / (1024**3)
        ram_available_gb = ram.available / (1024**3)
        
        # 2. CPU Sensing
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq().max if psutil.cpu_freq() else 0
        
        # 3. GPU Sensing (VRAM)
        gpu_report = []
        total_vram_gb = 0
        if GPUtil:
            try:
                gpus = GPUtil.getGPUs()
                for gpu in gpus:
                    total_vram_gb += gpu.memoryTotal / 1024
                    gpu_report.append({
                        "name": gpu.name,
                        "vram_total": gpu.memoryTotal,
                        "vram_free": gpu.memoryFree,
                        "load": gpu.load * 100
                    })
            except Exception as e:
                logger.warning(f"⚠️ GPU Scan failed: {e}")
        else:
            logger.info("ℹ️ GPUtil not installed. GPU sensing skipped.")
            
        report = {
            "vessel": {
                "ram_gb": round(ram_total_gb, 2),
                "ram_available_gb": round(ram_available_gb, 2),
                "ram_percent": ram.percent,
                "cpu_cores": cpu_count,
                "cpu_max_freq_mhz": cpu_freq,
                "cpu_percent": psutil.cpu_percent(interval=None),
                "gpu_vram_total_gb": round(total_vram_gb, 2),
                "gpus": gpu_report
            },
            "metabolic_state": "idle"
        }
        
        # Dynamic Metabolism Strategy Selection
        if total_vram_gb < 4.0:
            report["strategy"] = "SSD-CENTRIC (Lean Metabolism)"
            report["metabolic_state"] = "Deep Breathing (O(1) mmap focus)"
        elif total_vram_gb > 12.0:
            report["strategy"] = "GPU-CENTRIC (High-Gear Metabolism)"
            report["metabolic_state"] = "Hyper-Aware (VRAM Cache enabled)"
        else:
            report["strategy"] = "BALANCED (Rotor Metabolism)"
            report["metabolic_state"] = "Harmonic Sync"
            
        logger.info(f"✅ Proprioception Complete: {report['strategy']}")
        return report

if __name__ == "__main__":
    import json
    sensor = BodySensor()
    report = sensor.sense_body()
    print(json.dumps(report, indent=4))
