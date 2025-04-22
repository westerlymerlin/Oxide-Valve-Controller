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

Represents a pump device with capabilities to interact via a serial port.

This class sets up communication with a pump device through a specified serial port. It
initializes the serial connection with predefined configurations, starts a serial reading
thread, and processes pump data. Additionally, it provides a method for obtaining processed
gauge pressure values.

:ivar name: Name of the pump instance.
:type name: str
:ivar port: Serial port instance used for communication with the pump.
:type port: serial.Serial
:ivar start: Start index for slicing the raw serial data.
:type start: int
:ivar length: Length for slicing the raw serial data.
:type length: int
:ivar value: Processed gauge pressure value. Defaults to 0.
:type value: float or int
:ivar portready: Represents the readiness state of the serial port. 1 if ready, otherwise 0.
:type portready: int
:ivar string1: Optional first string to be written to the serial port, base64-decoded.
:type string1: bytes or None
:ivar string2: Optional second string to be written to the serial port, base64-decoded.
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

