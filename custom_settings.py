"""
A module for storing and managing configuration or custom settings.

This module provides a dictionary named `custom_settings` that can be
used to define and store custom configuration or settings. These settings
can be used across different parts of an application.

Attributes:
    custom_settings (dict): A dictionary to hold custom configuration
    settings, which can be set and accessed dynamically within the
    application.
"""

custom_settings = {
    'app-name': 'Oxide Line Valve Controller',
    'logappname': 'Valve-Controller-Py',
    'logfilepath': './logs/valvecontroller.log',
    'digital_prefix': 'digital',
    'digital_on_value': 'open',
    'digital_on_command': 'open',
    'digital_off_value': 'closed',
    'digital_off_command': 'close',
    'digital_channels': {
        '1': {
            'name': 'heating cell',
            'gpio': 23,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '2': {
            'name': 'Ar tank pipette input',
            'gpio': 22,
            'direction': 'output',
            'enabled': True,
            'excluded': '3',
            'pwm': 50,
            'frequency': 500
        },
        '3': {
            'name': 'Ar tank pipette output',
            'gpio': 27,
            'direction': 'output',
            'enabled': True,
            'excluded': '2',
            'pwm': 50,
            'frequency': 500
        },
        '4': {
            'name': 'Ne tank pipette input',
            'gpio': 18,
            'direction': 'output',
            'enabled': True,
            'excluded': '5',
            'pwm': 50,
            'frequency': 500
        },
        '5': {
            'name': 'Ne tank pipette output',
            'gpio': 17,
            'direction': 'output',
            'enabled': True,
            'excluded': '4',
            'pwm': 50,
            'frequency': 500
        },
        '6': {
            'name': '4He Q tank pipette input',
            'gpio': 13,
            'direction': 'output',
            'enabled': True,
            'excluded': '7',
            'pwm': 50,
            'frequency': 500
        },
        '7': {
            'name': '4He Q tank pipette output',
            'gpio': 12,
            'direction': 'output',
            'enabled': True,
            'excluded': '6',
            'pwm': 50,
            'frequency': 500
        },
        '8': {
            'name': '3He spike tank pipette input',
            'gpio': 11,
            'direction': 'output',
            'enabled': True,
            'excluded': '9',
            'pwm': 50,
            'frequency': 500
        },
        '9': {
            'name': '3He spike tank pipette output',
            'gpio': 9,
            'direction': 'output',
            'enabled': True,
            'excluded': '8',
            'pwm': 50,
            'frequency': 500
        },
        '10': {
            'name': 'turbo to cryotrap',
            'gpio': 24,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '11': {
            'name': 'input to manifold',
            'gpio': 21,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '12': {
            'name': 'turbo to manifold',
            'gpio': 20,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '13': {
            'name': 'SRS RGA',
            'gpio': 26,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '14': {
            'name': 'cold getter',
            'gpio': 16,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '15': {
            'name': 'ion pump',
            'gpio': 19,
            'direction': 'output',
            'enabled': True,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        },
        '16': {
            'name': 'Not Configured',
            'gpio': 25,
            'direction': 'input',
            'enabled': False,
            'excluded': '0',
            'pwm': 50,
            'frequency': 500
        }
    },
    'serial_channels': [
        {
            "api-name": "ion-pump",
            "baud": 9600,
            "mode": "interactive",
            "poll_interval": 10,
            "port": "/dev/ttyUSB0",
            "messages": [
                 {"api-command": "",
                  "length": -4,
                  "name": "Ion Pressure",
                  "start": 9,
                  "string1": "fiAwMSAwQiAzMw0=",
                  "string2": ""
                  },
                 {"api-command": "start",
                  "length": -4,
                  "name": "start",
                  "start": 3,
                  "string1": "fiAwMSAzNyAyQg0=",
                  "string2": ""
                  },
                 {"api-command": "",
                  "length": -4,
                  "name": "Ion Status",
                  "start": 9,
                  "string1": "fiAwMSAwRCAzNQ0=",
                  "string2": ""
                  },
                 {"api-command": "stop",
                  "length": -4,
                  "name": "stop",
                  "start": 3,
                  "string1": "fiAwMSAzOCAyQw0=",
                  "string2": ""
                  }
                ]
            },
            {"api-name": "turbo-pump",
            "baud": 9600,
            "mode": "listener",
            "poll_interval": 5,
            "port": "/dev/ttyUSB1",
            "messages": [
                 {"api-command": "",
                  "length": 7,
                  "name": "Turbo Model",
                  "start": 0,
                  "string1": "MDAxMTAzNDkwNg==",
                  "string2": ""
                  },
                 {"api-command": "",
                  "length": 7,
                  "name": "Turbo Pressure",
                  "start": 0,
                  "string1": "MDAxMTA3NDAwNg==",
                  "string2": ""
                  }
             ],
            }
    ]
}
