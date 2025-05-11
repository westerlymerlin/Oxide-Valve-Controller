# Module Documentation


This document contains the documentation for all the modules in the **Oxide Line Valve Controller** version 1.3.3 application.

---

## Contents


[app](./app.md)  
Flask web application for valve control system monitoring and management.

Provides web interface and REST API endpoints for:
- Valve status monitoring and control
- System statistics (CPU temperature, running threads)
- Log viewing (application, Gunicorn, and system logs)
- Real-time status updates

API access requires authentication via API key header.

[app_control](./app_control.md)  
Application control and configuration management.

Handles core application settings and version control for the valve control system.
Centralizes configuration management including:
- API authentication settings
- Application identification
- File paths and system locations
- Runtime configuration parameters

Configuration is loaded at module import time and remains constant during runtime.

[logmanager](./logmanager.md)  
Logging Configuration and Management

This module provides centralized logging configuration and management for the application.
Configures logging formats, handlers, and log file management to ensure consistent
logging across all application components.

Features:
    - Standardized log formatting
    - File-based logging with rotation
    - Log level management
    - Thread-safe logging operations

Exports:
    logger: Configured logger instance for use across the application

Usage:
    from logmanager import logger

    logger.info('Operation completed successfully')
    logger.warning('Resource threshold reached')
    logger.error('Failed to complete operation')

Log Format:
    Timestamps, log levels, and contextual information are automatically included
    in each log entry for effective debugging and monitoring.

Log Files:
    Logs are stored with automatic rotation to prevent excessive disk usage
    while maintaining historical records.

[pumpclass](./pumpclass.md)  
Vacuum pump control and monitoring class.

Provides object-oriented interface for managing pump systems:
- Pump start/stop control
- Runtime status monitoring
- Operating parameter validation
- Alarm condition handling
- System diagnostics
- State persistence

Class-based implementation ensures encapsulated pump management with
proper initialization, state tracking, and shutdown procedures.
Designed for integration with industrial control systems.

[rs485class](./rs485class.md)  
RS-485 serial communication interface module.

Provides a class-based interface for RS-485 serial communication with
industrial devices such as valves and sensors. Handles:
- RS-485 port configuration and management
- Serial protocol implementation
- Data framing and validation
- Transmission error detection
- Message queuing and timeout handling

This module implements thread-safe operations for reliable communication
over RS-485 networks in industrial control applications. Supports both
synchronous and asynchronous communication patterns.

[valvecontrol](./valvecontrol.md)  
Core valve control system interface module.

Provides hardware abstraction layer for valve monitoring and control operations:
- Real-time valve status monitoring and state management
- HTTP endpoint status checking and response handling
- Control command validation and execution
- System status reporting and error handling

All external valve interactions should go through this module to ensure
consistent state management and proper error handling. Implements thread-safe
operations for concurrent access.


---

