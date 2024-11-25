# UCL-Oxide-Valve-Controller

### Valve controller is a python app that can operate 24v valves and is controlled via an HTTP API


`app.py`			    Flask application that manages the API 

`valvecontrol.py`		python GPIO routine for setting up and managing 24v solonoid valves

<br><br>

---
### JSON Commands

| JSON | Description |                                                                      
|---|---|
| `{'status', '1'}`      | Return the status of all valves                                                                            |
| `{'valveN', 'open'}`   | Open valve N |
| `{'valveN', 'close'}` | lose valve N |
| `{'closeallvalves', 1}`  | close all valves and pipettes |


<br><br>

---
Full documentation can be found in the file: [README.pdf](./README.pdf)

Change log can be found in the file [changelog.txt](./changelog.txt)