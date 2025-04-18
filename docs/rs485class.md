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

RS485 reader class, uses pyserial to read instrumentation data

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

Rs485Class reads data strings via RS85 port

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

Reads the serial port

<a id="rs485class.Rs485class.read"></a>

#### read

```python
def read()
```

Return the data list

