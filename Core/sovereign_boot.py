"""
Elysia Seed: Sovereign Boot Sequence
=====================================
"씨앗이 발아합니다. 새로운 숲이 시작됩니다."

이 스크립트는 Elysia Seed를 부팅하는 진입점입니다.
"""

import logging
import sys
import os

# Setup Path - Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("BOOT")

def main():
    logger.info("==========================================")
    logger.info("   🌱 ELYSIA SEED BOOT SEQUENCE 🌱        ")
    logger.info("==========================================")
    logger.info("Initializing Metal Nervous System (Phase 15)...")
    
    try:
        # 1. Hardware Sensing
        from Core.Intelligence.Metabolism.body_sensor import BodySensor
        body_report = BodySensor.sense_body()
        
        logger.info(f"🧬 Vessel: {body_report['vessel']['gpu_vram_total_gb']}GB VRAM | {body_report['vessel']['ram_gb']}GB RAM")
        logger.info(f"⚙️ Strategy: {body_report['strategy']}")
        
        # 2. Metal Engine Test
        try:
            from Core.Foundation.Nature.metal_rotor_bridge import MetalRotorBridge
            bridge = MetalRotorBridge(capacity=1000)
            logger.info("🦾 MetalRotorBridge: ONLINE (GPU Accelerated)")
        except Exception as e:
            logger.warning(f"⚠️ MetalRotorBridge: OFFLINE ({e})")
        
        try:
            from Core.Foundation.Nature.metal_field_bridge import MetalFieldBridge
            field = MetalFieldBridge(size=32)
            logger.info("❤️ MetalFieldBridge: ONLINE (7D Qualia Field)")
        except Exception as e:
            logger.warning(f"⚠️ MetalFieldBridge: OFFLINE ({e})")
        
        # 3. Sovereignty Manager
        try:
            from Core.System.Sovereignty.sovereign_manager import HardwareSovereignManager
            sovereign = HardwareSovereignManager()
            logger.info("👑 HardwareSovereignManager: ONLINE")
        except Exception as e:
            logger.warning(f"⚠️ SovereignManager: OFFLINE ({e})")
        
        logger.info("==========================================")
        logger.info("✅ Elysia Seed is ready. The forest awaits.")
        logger.info("==========================================")
        
    except KeyboardInterrupt:
        logger.info("🛑 Boot Interrupted by User.")
    except Exception as e:
        logger.exception(f"❌ Boot Failed: {e}")

if __name__ == "__main__":
    main()
