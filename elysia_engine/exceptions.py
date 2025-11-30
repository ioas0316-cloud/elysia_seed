"""
Elysia Engine Custom Exceptions

Provides a hierarchy of custom exception classes for better error handling
and more informative error messages.

Usage:
    from elysia_engine.exceptions import (
        ElysiaError,
        TensorError,
        PhysicsError,
        ConfigurationError,
    )
    
    try:
        # some operation
    except TensorError as e:
        logger.error("Tensor operation failed: %s", e)
"""

from __future__ import annotations

from typing import Any, Dict, Optional


class ElysiaError(Exception):
    """
    Base exception for all Elysia Engine errors.
    
    All custom exceptions should inherit from this class.
    """
    
    def __init__(
        self,
        message: str,
        *,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize the exception.
        
        Args:
            message: Human-readable error message
            details: Optional dictionary with additional context
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}
    
    def __str__(self) -> str:
        if self.details:
            detail_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({detail_str})"
        return self.message


# ====================  Tensor-related Exceptions ====================

class TensorError(ElysiaError):
    """Base exception for tensor-related errors."""
    pass


class TensorCollapsedError(TensorError):
    """Raised when an operation is attempted on a collapsed tensor."""
    
    def __init__(self, operation: str, tensor_id: Optional[str] = None) -> None:
        details = {"operation": operation}
        if tensor_id:
            details["tensor_id"] = tensor_id
        super().__init__(
            f"Cannot perform '{operation}' on a collapsed tensor",
            details=details,
        )


class TensorInsufficientEnergyError(TensorError):
    """Raised when a tensor lacks sufficient energy for an operation."""
    
    def __init__(
        self,
        operation: str,
        required: float,
        available: float,
    ) -> None:
        super().__init__(
            f"Insufficient energy for '{operation}'",
            details={
                "operation": operation,
                "required": required,
                "available": available,
            },
        )


# ==================== Physics-related Exceptions ====================

class PhysicsError(ElysiaError):
    """Base exception for physics-related errors."""
    pass


class InvalidMassError(PhysicsError):
    """Raised when a mass value is invalid (zero or negative)."""
    
    def __init__(self, mass: float, context: Optional[str] = None) -> None:
        msg = f"Invalid mass value: {mass}"
        details: Dict[str, Any] = {"mass": mass}
        if context:
            msg = f"{msg} in {context}"
            details["context"] = context
        super().__init__(msg, details=details)


class BoundaryViolationError(PhysicsError):
    """Raised when an entity exceeds world boundaries."""
    
    def __init__(
        self,
        entity_id: str,
        position: tuple[float, float, float],
        boundary: tuple[float, float, float],
    ) -> None:
        super().__init__(
            f"Entity '{entity_id}' exceeded world boundary",
            details={
                "entity_id": entity_id,
                "position": position,
                "boundary": boundary,
            },
        )


# ==================== Entity-related Exceptions ====================

class EntityError(ElysiaError):
    """Base exception for entity-related errors."""
    pass


class EntityNotFoundError(EntityError):
    """Raised when an entity cannot be found."""
    
    def __init__(self, entity_id: str) -> None:
        super().__init__(
            f"Entity not found: '{entity_id}'",
            details={"entity_id": entity_id},
        )


class EntityAlreadyExistsError(EntityError):
    """Raised when attempting to create an entity with an existing ID."""
    
    def __init__(self, entity_id: str) -> None:
        super().__init__(
            f"Entity already exists: '{entity_id}'",
            details={"entity_id": entity_id},
        )


class InvalidEntityStateError(EntityError):
    """Raised when an entity is in an invalid state for an operation."""
    
    def __init__(
        self,
        entity_id: str,
        operation: str,
        current_state: str,
        required_state: str,
    ) -> None:
        super().__init__(
            f"Invalid state for '{operation}' on entity '{entity_id}'",
            details={
                "entity_id": entity_id,
                "operation": operation,
                "current_state": current_state,
                "required_state": required_state,
            },
        )


# ==================== Configuration Exceptions ====================

class ConfigurationError(ElysiaError):
    """Base exception for configuration-related errors."""
    pass


class MissingConfigurationError(ConfigurationError):
    """Raised when a required configuration value is missing."""
    
    def __init__(self, key: str, source: Optional[str] = None) -> None:
        msg = f"Missing required configuration: '{key}'"
        details: dict[str, Any] = {"key": key}
        if source:
            msg = f"{msg} in {source}"
            details["source"] = source
        super().__init__(msg, details=details)


class InvalidConfigurationError(ConfigurationError):
    """Raised when a configuration value is invalid."""
    
    def __init__(
        self,
        key: str,
        value: Any,
        reason: str,
    ) -> None:
        super().__init__(
            f"Invalid configuration for '{key}': {reason}",
            details={
                "key": key,
                "value": value,
                "reason": reason,
            },
        )


# ==================== System Exceptions ====================

class SystemError(ElysiaError):
    """Base exception for system-related errors."""
    pass


class SystemNotInitializedError(SystemError):
    """Raised when a system is used before initialization."""
    
    def __init__(self, system_name: str) -> None:
        super().__init__(
            f"System not initialized: '{system_name}'",
            details={"system_name": system_name},
        )


class SystemAlreadyRegisteredError(SystemError):
    """Raised when attempting to register a duplicate system."""
    
    def __init__(self, system_name: str) -> None:
        super().__init__(
            f"System already registered: '{system_name}'",
            details={"system_name": system_name},
        )


# ==================== Memory/Consciousness Exceptions ====================

class ConsciousnessError(ElysiaError):
    """Base exception for consciousness-related errors."""
    pass


class MemoryOverflowError(ConsciousnessError):
    """Raised when memory capacity is exceeded."""
    
    def __init__(
        self,
        memory_type: str,
        capacity: int,
        attempted_size: int,
    ) -> None:
        super().__init__(
            f"Memory overflow in '{memory_type}'",
            details={
                "memory_type": memory_type,
                "capacity": capacity,
                "attempted_size": attempted_size,
            },
        )


class EntanglementError(ConsciousnessError):
    """Raised when quantum entanglement fails."""
    
    def __init__(
        self,
        soul_a_id: str,
        soul_b_id: str,
        reason: str,
    ) -> None:
        super().__init__(
            f"Entanglement failed between '{soul_a_id}' and '{soul_b_id}'",
            details={
                "soul_a_id": soul_a_id,
                "soul_b_id": soul_b_id,
                "reason": reason,
            },
        )
