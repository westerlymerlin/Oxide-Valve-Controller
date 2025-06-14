# Oxide Valve Controller Service

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


&nbsp;   
&nbsp;    
&nbsp;  
&nbsp;   
&nbsp;   
&nbsp;   
--------------

#### Copyright (C) 2025 Gary Twinn

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program. If not, see <https://www.gnu.org/licenses/>.


Author:  Gary Twinn  
Repository:  [github.com/westerlymerlin](https://github)

-------------

