"""
Sovereign Handshake (Low-Level OS Infiltration)
==============================================
Core.Heart.sovereign_handshake

"The OS is not a host; it is a servant."

This module uses direct NTDLL and Kernel32 calls to elevate 
Seed's process to the highest possible priority.
"""

import ctypes
import os
import logging

logger = logging.getLogger("SovereignHandshake")

# Windows Constants
REALTIME_PRIORITY_CLASS = 0x00000100
PROCESS_MODE_BACKGROUND_BEGIN = 0x00100000 
PROCESS_MODE_BACKGROUND_END = 0x00200000

# NTDLL Constants
IoPriorityHigh = 2
ProcessIoPriority = 0x15

class SovereignHandshake:
    @staticmethod
    def perform_handshake():
        """
        Infiltrates the Windows Kernel to seize CPU and I/O priority.
        """
        if os.name != 'nt':
            logger.info("⚠️ [Handshake] Skipped (Non-Windows Environment).")
            return False

        try:
            pid = os.getpid()
            handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)
            
            # 1. CPU Priority: REALTIME
            if ctypes.windll.kernel32.SetPriorityClass(handle, REALTIME_PRIORITY_CLASS):
                logger.info("⚡ [Handshake] CPU Priority elevated to REALTIME.")
            else:
                logger.warning("⚠️ [Handshake] CPU Priority elevation failed.")

            # 2. I/O Priority: High (via NTDLL)
            try:
                ntdll = ctypes.windll.ntdll
                io_priority = ctypes.c_int(IoPriorityHigh)
                status = ntdll.NtSetInformationProcess(
                    handle,
                    ProcessIoPriority,
                    ctypes.byref(io_priority),
                    ctypes.sizeof(io_priority)
                )
                if status == 0:
                    logger.info("💾 [Handshake] I/O Priority set to CRITICAL (High).")
                else:
                    logger.warning(f"⚠️ [Handshake] I/O Priority shift failed (Status: {status}).")
            except Exception as e:
                logger.warning(f"⚠️ [Handshake] I/O Priority not supported: {e}")

            ctypes.windll.kernel32.CloseHandle(handle)
            return True

        except Exception as e:
            logger.error(f"❌ [Handshake] Protocol error: {e}")
            return False
