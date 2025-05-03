# Contents for: pumpclass

* [pumpclass](#pumpclass)
  * [sleep](#pumpclass.sleep)
  * [Timer](#pumpclass.Timer)
  * [b64decode](#pumpclass.b64decode)
  * [serial](#pumpclass.serial)
  * [logger](#pumpclass.logger)
  * [PumpClass](#pumpclass.PumpClass)
    * [\_\_init\_\_](#pumpclass.PumpClass.__init__)
    * [serialreader](#pumpclass.PumpClass.serialreader)
    * [read](#pumpclass.PumpClass.read)

<a id="pumpclass"></a>

# pumpclass

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

<a id="pumpclass.sleep"></a>

## sleep

<a id="pumpclass.Timer"></a>

## Timer

<a id="pumpclass.b64decode"></a>

## b64decode

<a id="pumpclass.serial"></a>

## serial

<a id="pumpclass.logger"></a>

## logger

<a id="pumpclass.PumpClass"></a>

## PumpClass Objects

```python
class PumpClass()
```

Represents a pump with serial communication capabilities, allowing for continuous
monitoring and data processing. The pump is initialized with various configuration
parameters, and its state is maintained via the serial connection. The class is
designed to continuously read data from the serial port, handle exceptions, and
maintain an internal value.

This class encapsulates serial port configuration, controls, and management for
interfacing with a pump device. It enables data writing, reading, and logging while
ensuring resilience to communication errors.

:ivar name: Name of the pump.
:type name: str
:ivar port: Serial port object configured for the pump.
:type port: serial.Serial
:ivar start: Starting position for slicing the read data.
:type start: int
:ivar length: Length of the data slice to extract from the read data.
:type length: int
:ivar commsdebug: Debug flag for logging detailed communication info.
:type commsdebug: bool
:ivar value: Extracted and processed data from the pump.
:type value: int or str
:ivar portready: Readiness state of the serial port (1 for ready, 0 otherwise).
:type portready: int
:ivar string1: Decoded pre-configured first string to write to the port.
:type string1: bytes or None
:ivar string2: Decoded pre-configured second string to write to the port.
:type string2: bytes or None

<a id="pumpclass.PumpClass.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name, port, speed, start, length, string1=None, string2=None)
```

<a id="pumpclass.PumpClass.serialreader"></a>

#### serialreader

```python
def serialreader()
```

Continuously reads data from a serial port and processes it based on the current
object's configuration and state. Writes pre-configured strings to the port
before reading data if applicable and logs the processed results. Handles
exceptions and sets a default value to indicate errors during operations.

:return: None

<a id="pumpclass.PumpClass.read"></a>

#### read

```python
def read()
```

Return the gauge pressure

