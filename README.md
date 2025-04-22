# UCL-Oxide-Valve-Controller

### Valve controller is a python app that can operate 24v valves and is controlled via an HTTP API


Application dcumentaton can be found in [manual.pdf](./manual.pdf)

Python module documentation can be found in the folder: [docs](./docs/readme.md)

Change log can be found in the file [changelog.txt](./changelog.txt)

---
### JSON Commands

| JSON                       | Description                              |                                                                      
|----------------------------|------------------------------------------|
| `{'valvestatus', '1'}`     | Return the status of all valves          |
| `{'valveN', 'open'}`       | Open valve N                             |
| `{'valveN', 'close'}`      | lose valve N                             |
| `{'closeallvalves', 1}`    | close all valves and pipettes            |
| `{'getpressures', 'read'}` | read pressures from turbo and ion gauges |


