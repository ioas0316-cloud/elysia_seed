"""
Tests for the new infrastructure modules:
- logging_config
- exceptions
- config
"""

import os
import tempfile
import pytest
import logging

from elysia_engine.logging_config import (
    get_logger,
    get_log_level,
    configure_root_logger,
    set_log_level,
)
from elysia_engine.exceptions import (
    ElysiaError,
    TensorError,
    TensorCollapsedError,
    TensorInsufficientEnergyError,
    PhysicsError,
    InvalidMassError,
    EntityError,
    EntityNotFoundError,
    ConfigurationError,
    MissingConfigurationError,
    InvalidConfigurationError,
)
from elysia_engine.config import (
    ElysiaConfig,
    PhysicsConfig,
    LoggingConfig,
    get_config,
    set_config,
    reset_config,
)


class TestLogging:
    """Tests for the logging configuration module."""
    
    def test_get_logger_creates_logger(self):
        """Test that get_logger creates a logger instance."""
        logger = get_logger("test.module")
        assert isinstance(logger, logging.Logger)
        assert logger.name == "test.module"
    
    def test_get_logger_returns_same_instance(self):
        """Test that get_logger returns the same logger for the same name."""
        logger1 = get_logger("test.same")
        logger2 = get_logger("test.same")
        assert logger1 is logger2
    
    def test_default_log_level(self):
        """Test that default log level is INFO."""
        # Clear environment variable if set
        old_value = os.environ.pop("ELYSIA_LOG_LEVEL", None)
        try:
            level = get_log_level()
            assert level == logging.INFO
        finally:
            if old_value is not None:
                os.environ["ELYSIA_LOG_LEVEL"] = old_value
    
    def test_log_level_from_env(self):
        """Test log level can be set from environment."""
        old_value = os.environ.get("ELYSIA_LOG_LEVEL")
        try:
            os.environ["ELYSIA_LOG_LEVEL"] = "DEBUG"
            level = get_log_level()
            assert level == logging.DEBUG
        finally:
            if old_value is not None:
                os.environ["ELYSIA_LOG_LEVEL"] = old_value
            else:
                os.environ.pop("ELYSIA_LOG_LEVEL", None)
    
    def test_configure_root_logger(self):
        """Test configuring the root logger."""
        configure_root_logger(level=logging.WARNING)
        root = logging.getLogger("elysia_engine")
        assert root.level == logging.WARNING


class TestExceptions:
    """Tests for custom exception classes."""
    
    def test_elysia_error_basic(self):
        """Test basic ElysiaError creation."""
        error = ElysiaError("Something went wrong")
        assert str(error) == "Something went wrong"
        assert error.message == "Something went wrong"
        assert error.details == {}
    
    def test_elysia_error_with_details(self):
        """Test ElysiaError with details."""
        error = ElysiaError(
            "Operation failed",
            details={"key": "value", "count": 42},
        )
        assert "key=value" in str(error)
        assert "count=42" in str(error)
    
    def test_tensor_collapsed_error(self):
        """Test TensorCollapsedError."""
        error = TensorCollapsedError("evolve", tensor_id="soul_001")
        assert "evolve" in str(error)
        assert "collapsed" in str(error).lower()
        assert error.details["tensor_id"] == "soul_001"
    
    def test_tensor_insufficient_energy_error(self):
        """Test TensorInsufficientEnergyError."""
        error = TensorInsufficientEnergyError("split", required=100.0, available=50.0)
        assert error.details["required"] == 100.0
        assert error.details["available"] == 50.0
    
    def test_invalid_mass_error(self):
        """Test InvalidMassError."""
        error = InvalidMassError(-1.5, context="entity creation")
        assert "-1.5" in str(error)
        assert error.details["mass"] == -1.5
    
    def test_entity_not_found_error(self):
        """Test EntityNotFoundError."""
        error = EntityNotFoundError("entity_123")
        assert "entity_123" in str(error)
        assert error.details["entity_id"] == "entity_123"
    
    def test_missing_configuration_error(self):
        """Test MissingConfigurationError."""
        error = MissingConfigurationError("api_key", source="config.yaml")
        assert "api_key" in str(error)
        assert "config.yaml" in str(error)
    
    def test_invalid_configuration_error(self):
        """Test InvalidConfigurationError."""
        error = InvalidConfigurationError(
            key="gravity",
            value=-100,
            reason="must be positive",
        )
        assert error.details["key"] == "gravity"
        assert error.details["value"] == -100
    
    def test_exception_inheritance(self):
        """Test exception hierarchy."""
        assert issubclass(TensorError, ElysiaError)
        assert issubclass(PhysicsError, ElysiaError)
        assert issubclass(EntityError, ElysiaError)
        assert issubclass(ConfigurationError, ElysiaError)


class TestConfig:
    """Tests for configuration management."""
    
    def setup_method(self):
        """Reset config before each test."""
        reset_config()
    
    def teardown_method(self):
        """Reset config after each test."""
        reset_config()
    
    def test_default_physics_config(self):
        """Test default physics configuration values."""
        config = PhysicsConfig()
        assert config.gravity_constant == 1.0
        assert config.coupling_constant == 0.5
        assert config.time_scale == 1.0
        assert config.max_gravity == 50.0
    
    def test_default_logging_config(self):
        """Test default logging configuration."""
        config = LoggingConfig()
        assert config.level == "INFO"
        assert config.format == "default"
        assert config.level_value == logging.INFO
    
    def test_elysia_config_defaults(self):
        """Test default ElysiaConfig."""
        config = ElysiaConfig()
        assert config.physics.gravity_constant == 1.0
        assert config.logging.level == "INFO"
        assert config.debug_mode is False
        assert config.seed is None
    
    def test_config_from_dict(self):
        """Test creating config from dictionary."""
        data = {
            "physics": {
                "gravity_constant": 2.5,
                "coupling_constant": 0.8,
            },
            "logging": {
                "level": "DEBUG",
            },
            "debug_mode": True,
        }
        config = ElysiaConfig.from_dict(data)
        assert config.physics.gravity_constant == 2.5
        assert config.physics.coupling_constant == 0.8
        assert config.logging.level == "DEBUG"
        assert config.debug_mode is True
    
    def test_config_to_dict(self):
        """Test converting config to dictionary."""
        config = ElysiaConfig()
        config.physics.gravity_constant = 3.0
        config.debug_mode = True
        
        data = config.to_dict()
        assert data["physics"]["gravity_constant"] == 3.0
        assert data["debug_mode"] is True
    
    def test_config_save_and_load(self):
        """Test saving and loading config from file."""
        config = ElysiaConfig()
        config.physics.gravity_constant = 5.0
        config.logging.level = "WARNING"
        
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            config.save(f.name)
            
            loaded = ElysiaConfig.from_file(f.name)
            assert loaded.physics.gravity_constant == 5.0
            assert loaded.logging.level == "WARNING"
            
            os.unlink(f.name)
    
    def test_config_from_nonexistent_file(self):
        """Test loading from nonexistent file returns defaults."""
        config = ElysiaConfig.from_file("/nonexistent/path/config.json")
        assert config.physics.gravity_constant == 1.0  # Default value
    
    def test_get_config_singleton(self):
        """Test get_config returns singleton."""
        config1 = get_config()
        config2 = get_config()
        assert config1 is config2
    
    def test_set_config(self):
        """Test setting global config."""
        custom = ElysiaConfig()
        custom.physics.gravity_constant = 10.0
        
        set_config(custom)
        
        assert get_config().physics.gravity_constant == 10.0
    
    def test_config_from_env(self):
        """Test loading config from environment variables."""
        old_values = {}
        env_vars = {
            "ELYSIA_PHYSICS_GRAVITY_CONSTANT": "7.5",
            "ELYSIA_LOG_LEVEL": "WARNING",
            "ELYSIA_DEBUG_MODE": "true",
        }
        
        # Save old values
        for key in env_vars:
            old_values[key] = os.environ.get(key)
            os.environ[key] = env_vars[key]
        
        try:
            config = ElysiaConfig.from_env()
            assert config.physics.gravity_constant == 7.5
            assert config.logging.level == "WARNING"
            assert config.debug_mode is True
        finally:
            # Restore old values
            for key in env_vars:
                if old_values[key] is not None:
                    os.environ[key] = old_values[key]
                else:
                    os.environ.pop(key, None)
