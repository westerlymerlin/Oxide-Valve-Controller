# Contents for: rs485class

* [rs485class](#rs485class)
  * [sleep](#rs485class.sleep)
  * [Timer](#rs485class.Timer)
  * [serial](#rs485class.serial)
  * [settings](#rs485class.settings)
  * [logger](#rs485class.logger)
  * [Rs485class](#rs485class.Rs485class)
    * [\_\_init\_\_](#rs485class.Rs485class.__init__)
    * [rs485\_reader](#rs485class.Rs485class.rs485_reader)
    * [read](#rs485class.Rs485class.read)

<a id="rs485class"></a>

# rs485class

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

<a id="rs485class.sleep"></a>

## sleep

<a id="rs485class.Timer"></a>

## Timer

<a id="rs485class.serial"></a>

## serial

<a id="rs485class.settings"></a>

## settings

<a id="rs485class.logger"></a>

## logger

<a id="rs485class.Rs485class"></a>

## Rs485class Objects

```python
class Rs485class()
```

Handles RS485 communication and facilitates reading data from the serial port.

This class is designed to work with RS485 serial communication. It allows
for initializing a serial port, reading data from the port with a specified
interval, and parsing the data based on predefined readings. It operates with
an internal threading mechanism to continually read from the serial port in
the background.

:ivar port: Serial port object for RS485 communication.
:type port: serial.Serial
:ivar interval: Interval in seconds between consecutive reads from the port.
:type interval: float
:ivar readings: List of dictionaries containing metadata for parsing
                specific strings from the incoming data.
:type readings: list[dict]
:ivar readlength: Number of bytes to read from the serial port at a time.
:type readlength: int
:ivar data: List of dictionaries containing parsed data from the port.
:type data: list[dict]
:ivar portready: Flag indicating if the serial port is successfully opened and ready.
:type portready: int

<a id="rs485class.Rs485class.__init__"></a>

#### \_\_init\_\_

```python
def __init__(port, speed, interval, readlength, readings)
```

<a id="rs485class.Rs485class.rs485_reader"></a>

#### rs485\_reader

```python
def rs485_reader()
```

Continuously reads data from an RS485 device, processing and extracting relevant
information from the data stream. The method handles data parsing, error management,
and executes at a regular interval defined by the `interval` attribute.

The method checks if the port is ready, resets the input buffer, and reads data
of the specified length. It parses the incoming data based on configuration and
extracts key information for further use. Errors during the process are logged,
and the method safely retries after encountering issues.

:raises Exception: If there is an issue with reading the data or accessing the
    port.
:returns: None

<a id="rs485class.Rs485class.read"></a>

#### read

```python
def read()
```

Return the data list

