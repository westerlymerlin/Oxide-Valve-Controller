# UCL-Oxide-Valve-Controller

## Overview

A Python application that controls 24V valves through an HTTP API interface. This controller allows for remote operation
of valve systems in laboratory environments.

## Documentation

- **User Manual**: Detailed usage instructions can be found in [manual.pdf](./manual.pdf)
- **API Documentation**: Python module documentation is available in the [docs](./docs/readme.md) folder
- **Change Log**: Track version changes in the [changelog.txt](./changelog.txt) file

## API Commands

The controller accepts the following JSON commands:

| JSON Command | Description |
|-------------|-------------|
| `{"valvestatus": "1"}` | Return the status of all valves |
| `{"valveN": "open"}` | Open valve N (replace N with valve number) |
| `{"valveN": "close"}` | Close valve N (replace N with valve number) |
| `{"closeallvalves": 1}` | Close all valves and pipettes |
| `{"getpressures": "read"}` | Read pressures from turbo and ion gauges |


