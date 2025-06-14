# None

<a id="valvecontrol"></a>

# valvecontrol

Core valve control system interface module.

Provides hardware abstraction layer for valve monitoring and control operations:
- Real-time valve status monitoring and state management
- HTTP endpoint status checking and response handling
- Control command validation and execution
- System status reporting and error handling

All external valve interactions should go through this module to ensure
consistent state management and proper error handling. Implements thread-safe
operations for concurrent access.

<a id="valvecontrol.Timer"></a>

## Timer

<a id="valvecontrol.os"></a>

## os

<a id="valvecontrol.GPIO"></a>

## GPIO

<a id="valvecontrol.logger"></a>

## logger

<a id="valvecontrol.settings"></a>

## settings

<a id="valvecontrol.updatesetting"></a>

## updatesetting

<a id="valvecontrol.PumpClass"></a>

## PumpClass

<a id="valvecontrol.Rs485class"></a>

## Rs485class

<a id="valvecontrol.channellist"></a>

#### channellist

<a id="valvecontrol.valves"></a>

#### valves

<a id="valvecontrol.parsecontrol"></a>

#### parsecontrol

```python
def parsecontrol(item, command)
```

Parser that recieves messages from the API or web page posts and directs
messages to the correct function

<a id="valvecontrol.valveopen"></a>

#### valveopen

```python
def valveopen(valveid)
```

Opens a valve given its identifier. If the valve has an excluded valve
that is already open, it logs a warning and does not open the specified
valve. Otherwise, it proceeds to open the valve and logs the action.

:param valveid: Identifier of the valve to be opened
:type valveid: int
:return: None

<a id="valvecontrol.valveclose"></a>

#### valveclose

```python
def valveclose(valveid)
```

Close the valve specified

<a id="valvecontrol.allclose"></a>

#### allclose

```python
def allclose()
```

Close all valves

<a id="valvecontrol.status"></a>

#### status

```python
def status(value)
```

Meaningful value name for the specified valve

<a id="valvecontrol.valvestatus"></a>

#### valvestatus

```python
def valvestatus()
```

Return the status of all valves as a jason message

<a id="valvecontrol.httpstatus"></a>

#### httpstatus

```python
def httpstatus()
```

Status message formetted for the web status page

<a id="valvecontrol.statusmessage"></a>

#### statusmessage

```python
def statusmessage()
```

Return the status of all valves as a jason message

<a id="valvecontrol.reboot"></a>

#### reboot

```python
def reboot()
```

API call to reboot the Raspberry Pi

<a id="valvecontrol.get_turbo_gauge_pressure"></a>

#### get\_turbo\_gauge\_pressure

```python
def get_turbo_gauge_pressure()
```

API call: return the turbo gauge pressure as a JSON message.

<a id="valvecontrol.pressures"></a>

#### pressures

```python
def pressures()
```

API call: return all guage pressures as a json message

<a id="valvecontrol.http_pump"></a>

#### http\_pump

```python
def http_pump()
```

Web page setup for pump data

<a id="valvecontrol.turbopump"></a>

#### turbopump

<a id="valvecontrol.ionpump"></a>

#### ionpump

