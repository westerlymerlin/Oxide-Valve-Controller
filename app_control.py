
"""
Application control and configuration management.

Handles core application settings and version control for the valve control system.
Centralizes configuration management including:
- API authentication settings
- Application identification
- File paths and system locations
- Runtime configuration parameters

Configuration is loaded at module import time and remains constant during runtime.
"""
import random
import json
from datetime import datetime

VERSION = '1.3.0'

def initialise():
    """Setup the settings structure with default values"""
    isettings = {'LastSave': '01/01/2000 00:00:01',
                 'api-key': 'change-me',
                 'app-name': 'Oxide Line Valve Controller',
                 'logfilepath': './logs/valvecontroller.log',
                 'logappname': 'Valve-Controller-Py',
                 'loglevel': 'INFO',
                 'gunicornpath': './logs/',
                 'cputemp': '/sys/class/thermal/thermal_zone0/temp',
                 'ion-messages': [
                     {'name': 'pressure', 'string': 'fiAwMSAwQiAzMw0K', 'start': 9, 'length': 16, 'units': 'torr'},
                     {'name': 'status', 'string': 'fiAwMSAwRCAzNQ0K', 'start': 0, 'length': 16, 'units': ''},
                     {'name': 'start', 'string': 'fiAwMSAzNyAyQg0K', 'start': 0, 'length': 0, 'units': ''},
                     {'name': 'stop', 'string': 'fiAwMSAzOCAyQw0K', 'start': 0, 'length': 0, 'units': ''}
                 ],
                 'ion-length': 16,
                 'ion-port': '/dev/ttyUSB0',
                 'ion-speed': 9600,
                 'ion-start': 9,
                 'ion-string': 'fiAwMSAwQiAzMw0K',  # base64 encoded, pump id 01
                 'ion-units': 'mbar',
                 'rs485-readlength': 400,
                 'rs485-port': '/dev/ttyUSB1',
                 'rs485-speed': 9600,
                 'rs485-interval': 5,
                 'rs485-debug': False,
                 'rs485-messages': [
                     {'name': 'Turbo Gauge Pressure', 'string': '0011074006', 'length': 7, 'units': 'hPa'},
                     {'name': 'Turbo Gauge Model', 'string': '0011034906', 'length': 7, 'units': ''},
                 ]}
    return isettings


def generate_api_key(key_len):
    """generate a new api key"""
    allowed_characters = "ABCDEFGHJKLMNPQRSTUVWXYZ-+~abcdefghijkmnopqrstuvwxyz123456789"
    return ''.join(random.choice(allowed_characters) for _ in range(key_len))


def writesettings():
    """Write settings to json file"""
    settings['LastSave'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('settings.json', 'w', encoding='utf-8') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)


def readsettings():
    """Read the json file"""
    try:
        with open('settings.json', 'r', encoding='utf-8') as json_file:
            jsettings = json.load(json_file)
            return jsettings
    except FileNotFoundError:
        print('File not found')
        return {}

def updatesetting(newsetting): # must be a dict object
    """Update the settings with the new values"""
    global settings
    if isinstance(newsetting, dict):
        for item in newsetting.keys():
            settings[item] = newsetting[item]
        writesettings()

def loadsettings():
    """Replace the default settings with thsoe from the json files"""
    global settings
    settingschanged = False
    fsettings = readsettings()
    for item in settings.keys():
        try:
            settings[item] = fsettings[item]
        except KeyError:
            print('settings[%s] Not found in json file using default' % item)
            settingschanged = True
    if settings['api-key'] == 'change-me':
        settings['api-key'] = generate_api_key(128)
        settingschanged = True
    if settingschanged:
        writesettings()


settings = initialise()
loadsettings()
