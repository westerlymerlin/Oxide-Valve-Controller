# Contents for: pumpclass

* [pumpclass](#pumpclass)
  * [sleep](#pumpclass.sleep)
  * [Timer](#pumpclass.Timer)
  * [b64decode](#pumpclass.b64decode)
  * [serial](#pumpclass.serial)
  * [logger](#pumpclass.logger)
  * [PumpClass](#pumpclass.PumpClass)
    * [\_\_init\_\_](#pumpclass.PumpClass.__init__)
    * [pressurereader](#pumpclass.PumpClass.pressurereader)
    * [access\_pump](#pumpclass.PumpClass.access_pump)
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

Represents a serial communication interface for interacting with a pump.

This class facilitates communication with a pump device over a serial port. It is designed
to initialize the connection, handle exceptions during operations, and perform tasks such
as writing to the port or reading data from it. It includes functionalities to process
configured messages, monitor the state of the device, and retrieve or parse its data.

:ivar name: The name associated with the pump instance.
:type name: str
:ivar port: The serial port used for pump communication.
:type port: serial.Serial
:ivar messages: A list of pre-configured message dictionaries for operation requests.
:type messages: list[dict]
:ivar commsdebug: A flag for enabling or disabling detailed communication logging.
:type commsdebug: bool
:ivar pressurevalue: The current value retrieved or processed from the pump's response.
:type pressurevalue: str or int
:ivar portready: Indicates the readiness of the serial port. 1 if ready, 0 otherwise.
:type portready: int

<a id="pumpclass.PumpClass.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name, port, speed, messages)
```

<a id="pumpclass.PumpClass.pressurereader"></a>

#### pressurereader

```python
def pressurereader()
```

Reads and updates the pressure value and its units from an external pump
device at regular intervals of 5 seconds, provided the port is ready for
operation.

<a id="pumpclass.PumpClass.access_pump"></a>

#### access\_pump

```python
def access_pump(req_type)
```

Accesses a pump device, sends a request, and retrieves the corresponding response based
on the specified request type. The function interacts with hardware through a communication
port and processes the returned data to extract useful information.

:param req_type: The name of the request type to access on the pump.
:type req_type: str
:return: A dictionary containing the result of the pump access operation. The dictionary
    may either indicate the success of the request or include specific response data
    based on the length and type of the response.
:rtype: dict

<a id="pumpclass.PumpClass.read"></a>

#### read

```python
def read()
```

Reads and converts the stored value to a floating-point number.

This method attempts to parse the stored `value` attribute as a
floating-point number. If the value is an empty string, it will
return 0. If the conversion to a floating-point number fails,
it will also return 0.

:return: Returns the converted floating-point number from the
         value attribute or 0 if the conversion fails.
:rtype: float

