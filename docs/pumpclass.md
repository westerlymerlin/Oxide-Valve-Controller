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

Pump reader class, uses pyserial to read pressure gauges and pyrometer

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

PumpClass: reads pressures from gauges via RS232 ports

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

Reads the serial port

<a id="pumpclass.PumpClass.read"></a>

#### read

```python
def read()
```

Return the gauge pressure

