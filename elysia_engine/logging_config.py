"""
Elysia Engine Logging Configuration

Provides a centralized logging system for the engine, replacing scattered print()
statements with structured, level-based logging.

Usage:
    from elysia_engine.logging_config import get_logger
    
    logger = get_logger(__name__)
    logger.info("System started")
    logger.debug("Processing entity: %s", entity_id)
    logger.warning("Entropy critical: %.2f", entropy_value)
"""

from __future__ import annotations

import logging
import os
import sys
from typing import Optional


# Default logging format
DEFAULT_FORMAT = "[%(levelname)s] %(name)s: %(message)s"
DETAILED_FORMAT = "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"

# Environment variable to control log level
LOG_LEVEL_ENV = "ELYSIA_LOG_LEVEL"
LOG_FORMAT_ENV = "ELYSIA_LOG_FORMAT"


def get_log_level() -> int:
    """
    Get the log level from environment variable or default to INFO.
    
    Returns:
        Logging level constant
    """
    level_name = os.environ.get(LOG_LEVEL_ENV, "INFO").upper()
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    return level_map.get(level_name, logging.INFO)


def get_log_format() -> str:
    """
    Get the log format from environment variable or default.
    
    Returns:
        Format string for logging
    """
    format_type = os.environ.get(LOG_FORMAT_ENV, "default").lower()
    if format_type == "detailed":
        return DETAILED_FORMAT
    return DEFAULT_FORMAT


# Module-level logger cache to avoid creating duplicate loggers
_loggers: dict[str, logging.Logger] = {}


def get_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """
    Get or create a logger with the specified name.
    
    Args:
        name: Logger name (typically __name__ of the calling module)
        level: Optional override for log level
        
    Returns:
        Configured logger instance
    """
    if name in _loggers:
        return _loggers[name]
    
    logger = logging.getLogger(name)
    
    # Only configure if no handlers exist (avoid duplicate handlers)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter(get_log_format()))
        logger.addHandler(handler)
    
    logger.setLevel(level if level is not None else get_log_level())
    logger.propagate = False
    
    _loggers[name] = logger
    return logger


def configure_root_logger(
    level: Optional[int] = None,
    format_string: Optional[str] = None,
) -> None:
    """
    Configure the root logger for the entire engine.
    
    Call this at application startup to set up logging globally.
    
    Args:
        level: Log level (default: from environment or INFO)
        format_string: Log format (default: from environment or DEFAULT_FORMAT)
    """
    root_logger = logging.getLogger("elysia_engine")
    
    # Clear existing handlers
    root_logger.handlers.clear()
    
    handler = logging.StreamHandler(sys.stderr)
    fmt = format_string if format_string else get_log_format()
    handler.setFormatter(logging.Formatter(fmt))
    root_logger.addHandler(handler)
    
    log_level = level if level is not None else get_log_level()
    root_logger.setLevel(log_level)
    
    # Also configure elysia_core
    core_logger = logging.getLogger("elysia_core")
    core_logger.handlers.clear()
    core_handler = logging.StreamHandler(sys.stderr)
    core_handler.setFormatter(logging.Formatter(fmt))
    core_logger.addHandler(core_handler)
    core_logger.setLevel(log_level)


def set_log_level(level: int) -> None:
    """
    Dynamically change the log level for all elysia loggers.
    
    Args:
        level: New logging level
    """
    for logger in _loggers.values():
        logger.setLevel(level)
    
    # Also set on root loggers
    logging.getLogger("elysia_engine").setLevel(level)
    logging.getLogger("elysia_core").setLevel(level)
