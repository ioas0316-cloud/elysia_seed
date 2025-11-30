"""
Elysia Engine Configuration Management

Provides centralized configuration management with support for:
- Environment variables
- Configuration files (YAML/JSON)
- Default values
- Type validation

Usage:
    from elysia_engine.config import get_config, ElysiaConfig
    
    # Get the global config instance
    config = get_config()
    
    # Access values
    gravity = config.physics.gravity_constant
    log_level = config.logging.level
    
    # Or create a custom config
    custom_config = ElysiaConfig(gravity_constant=2.0)
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional, Union


# Environment variable prefix
ENV_PREFIX = "ELYSIA_"


@dataclass
class PhysicsConfig:
    """Physics system configuration."""
    
    gravity_constant: float = 1.0
    coupling_constant: float = 0.5
    time_scale: float = 1.0
    max_gravity: float = 50.0
    epsilon: float = 0.1
    
    # Thermodynamics
    ambient_temperature: float = 20.0
    cooling_rate: float = 0.01
    heat_transfer_rate: float = 0.1
    
    # Quantum
    decoherence_rate: float = 0.001
    tunneling_probability_scale: float = 0.1


@dataclass
class ConsciousnessConfig:
    """Consciousness system configuration."""
    
    entropy_threshold: float = 0.8
    alignment_threshold: float = 0.9
    intervention_cooldown: int = 50
    
    # Memory
    max_recent_thoughts: int = 10
    experience_loop_size: int = 100
    essence_loop_size: int = 7


@dataclass
class LoggingConfig:
    """Logging configuration."""
    
    level: str = "INFO"
    format: str = "default"
    
    @property
    def level_value(self) -> int:
        """Get logging level as integer."""
        import logging
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        return level_map.get(self.level.upper(), logging.INFO)


@dataclass
class ElysiaConfig:
    """
    Main configuration class for the Elysia Engine.
    
    Configuration is loaded from multiple sources in order of priority:
    1. Explicit constructor arguments (highest priority)
    2. Environment variables (ELYSIA_*)
    3. Configuration file (config.yaml or config.json)
    4. Default values (lowest priority)
    """
    
    physics: PhysicsConfig = field(default_factory=PhysicsConfig)
    consciousness: ConsciousnessConfig = field(default_factory=ConsciousnessConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    
    # General settings
    seed: Optional[int] = None
    debug_mode: bool = False
    
    @classmethod
    def from_env(cls) -> ElysiaConfig:
        """
        Create configuration from environment variables.
        
        Environment variables use the format: ELYSIA_SECTION_KEY
        Examples:
            ELYSIA_PHYSICS_GRAVITY_CONSTANT=2.0
            ELYSIA_LOGGING_LEVEL=DEBUG
            ELYSIA_DEBUG_MODE=true
        """
        config = cls()
        
        # Physics config
        config.physics.gravity_constant = _get_env_float(
            "PHYSICS_GRAVITY_CONSTANT",
            config.physics.gravity_constant,
        )
        config.physics.coupling_constant = _get_env_float(
            "PHYSICS_COUPLING_CONSTANT",
            config.physics.coupling_constant,
        )
        config.physics.time_scale = _get_env_float(
            "PHYSICS_TIME_SCALE",
            config.physics.time_scale,
        )
        config.physics.max_gravity = _get_env_float(
            "PHYSICS_MAX_GRAVITY",
            config.physics.max_gravity,
        )
        
        # Consciousness config
        config.consciousness.entropy_threshold = _get_env_float(
            "CONSCIOUSNESS_ENTROPY_THRESHOLD",
            config.consciousness.entropy_threshold,
        )
        config.consciousness.intervention_cooldown = _get_env_int(
            "CONSCIOUSNESS_INTERVENTION_COOLDOWN",
            config.consciousness.intervention_cooldown,
        )
        
        # Logging config
        config.logging.level = _get_env_str(
            "LOG_LEVEL",
            config.logging.level,
        )
        config.logging.format = _get_env_str(
            "LOG_FORMAT",
            config.logging.format,
        )
        
        # General
        config.debug_mode = _get_env_bool("DEBUG_MODE", config.debug_mode)
        seed_str = os.environ.get(f"{ENV_PREFIX}SEED")
        if seed_str is not None:
            try:
                config.seed = int(seed_str)
            except ValueError:
                pass
        
        return config
    
    @classmethod
    def from_file(cls, path: Union[str, Path]) -> ElysiaConfig:
        """
        Load configuration from a file.
        
        Supports JSON format.
        
        Args:
            path: Path to configuration file
            
        Returns:
            ElysiaConfig instance
        """
        path = Path(path)
        
        if not path.exists():
            return cls()
        
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        
        return cls.from_dict(data)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ElysiaConfig:
        """
        Create configuration from a dictionary.
        
        Args:
            data: Configuration dictionary
            
        Returns:
            ElysiaConfig instance
        """
        config = cls()
        
        # Physics
        if "physics" in data:
            physics = data["physics"]
            if "gravity_constant" in physics:
                config.physics.gravity_constant = float(physics["gravity_constant"])
            if "coupling_constant" in physics:
                config.physics.coupling_constant = float(physics["coupling_constant"])
            if "time_scale" in physics:
                config.physics.time_scale = float(physics["time_scale"])
            if "max_gravity" in physics:
                config.physics.max_gravity = float(physics["max_gravity"])
            if "ambient_temperature" in physics:
                config.physics.ambient_temperature = float(physics["ambient_temperature"])
            if "cooling_rate" in physics:
                config.physics.cooling_rate = float(physics["cooling_rate"])
        
        # Consciousness
        if "consciousness" in data:
            consciousness = data["consciousness"]
            if "entropy_threshold" in consciousness:
                config.consciousness.entropy_threshold = float(
                    consciousness["entropy_threshold"]
                )
            if "alignment_threshold" in consciousness:
                config.consciousness.alignment_threshold = float(
                    consciousness["alignment_threshold"]
                )
            if "intervention_cooldown" in consciousness:
                config.consciousness.intervention_cooldown = int(
                    consciousness["intervention_cooldown"]
                )
            if "max_recent_thoughts" in consciousness:
                config.consciousness.max_recent_thoughts = int(
                    consciousness["max_recent_thoughts"]
                )
        
        # Logging
        if "logging" in data:
            logging_cfg = data["logging"]
            if "level" in logging_cfg:
                config.logging.level = str(logging_cfg["level"])
            if "format" in logging_cfg:
                config.logging.format = str(logging_cfg["format"])
        
        # General
        if "debug_mode" in data:
            config.debug_mode = bool(data["debug_mode"])
        if "seed" in data and data["seed"] is not None:
            config.seed = int(data["seed"])
        
        return config
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to a dictionary.
        
        Returns:
            Configuration dictionary
        """
        return {
            "physics": {
                "gravity_constant": self.physics.gravity_constant,
                "coupling_constant": self.physics.coupling_constant,
                "time_scale": self.physics.time_scale,
                "max_gravity": self.physics.max_gravity,
                "ambient_temperature": self.physics.ambient_temperature,
                "cooling_rate": self.physics.cooling_rate,
                "heat_transfer_rate": self.physics.heat_transfer_rate,
                "decoherence_rate": self.physics.decoherence_rate,
            },
            "consciousness": {
                "entropy_threshold": self.consciousness.entropy_threshold,
                "alignment_threshold": self.consciousness.alignment_threshold,
                "intervention_cooldown": self.consciousness.intervention_cooldown,
                "max_recent_thoughts": self.consciousness.max_recent_thoughts,
                "experience_loop_size": self.consciousness.experience_loop_size,
                "essence_loop_size": self.consciousness.essence_loop_size,
            },
            "logging": {
                "level": self.logging.level,
                "format": self.logging.format,
            },
            "debug_mode": self.debug_mode,
            "seed": self.seed,
        }
    
    def save(self, path: Union[str, Path]) -> None:
        """
        Save configuration to a file.
        
        Args:
            path: Path to save configuration
        """
        path = Path(path)
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)


# Helper functions for environment variable parsing

def _get_env_str(key: str, default: str) -> str:
    """Get string from environment."""
    return os.environ.get(f"{ENV_PREFIX}{key}", default)


def _get_env_float(key: str, default: float) -> float:
    """Get float from environment."""
    value = os.environ.get(f"{ENV_PREFIX}{key}")
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def _get_env_int(key: str, default: int) -> int:
    """Get integer from environment."""
    value = os.environ.get(f"{ENV_PREFIX}{key}")
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _get_env_bool(key: str, default: bool) -> bool:
    """Get boolean from environment."""
    value = os.environ.get(f"{ENV_PREFIX}{key}")
    if value is None:
        return default
    return value.lower() in ("true", "1", "yes", "on")


# Global configuration instance
_global_config: Optional[ElysiaConfig] = None


def get_config() -> ElysiaConfig:
    """
    Get the global configuration instance.
    
    Creates a new instance from environment if not already initialized.
    
    Returns:
        Global ElysiaConfig instance
    """
    global _global_config
    if _global_config is None:
        _global_config = ElysiaConfig.from_env()
    return _global_config


def set_config(config: ElysiaConfig) -> None:
    """
    Set the global configuration instance.
    
    Args:
        config: Configuration to use globally
    """
    global _global_config
    _global_config = config


def reset_config() -> None:
    """Reset the global configuration to None (will be recreated on next get)."""
    global _global_config
    _global_config = None
