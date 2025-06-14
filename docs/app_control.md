# None

<a id="app_control"></a>

# app\_control

Application control and configuration management.

Handles core application settings and version control for the valve control system.
Centralizes configuration management including:
- API authentication settings
- Application identification
- File paths and system locations
- Runtime configuration parameters

Configuration is loaded at module import time and remains constant during runtime.

<a id="app_control.random"></a>

## random

<a id="app_control.json"></a>

## json

<a id="app_control.datetime"></a>

## datetime

<a id="app_control.VERSION"></a>

#### VERSION

<a id="app_control.initialise"></a>

#### initialise

```python
def initialise()
```

Setup the settings structure with default values

<a id="app_control.generate_api_key"></a>

#### generate\_api\_key

```python
def generate_api_key(key_len)
```

generate a new api key

<a id="app_control.writesettings"></a>

#### writesettings

```python
def writesettings()
```

Write settings to json file

<a id="app_control.readsettings"></a>

#### readsettings

```python
def readsettings()
```

Read the json file

<a id="app_control.updatesetting"></a>

#### updatesetting

```python
def updatesetting(newsetting)
```

Update the settings with the new values

<a id="app_control.loadsettings"></a>

#### loadsettings

```python
def loadsettings()
```

Replace the default settings with thsoe from the json files

<a id="app_control.settings"></a>

#### settings

