"""
Application control and configuration management for the Raspberry Pi control system.

This module manages core application configuration, settings, and version information
for the Flask-based control system. It handles loading and maintaining application-wide
settings that define crucial operational parameters.

Attributes:
    VERSION (str): The current version of the application
    settings (dict): Application-wide configuration dictionary containing:
        - app-name (str): Application identifier used in logging and display
        - api-key (str): Authentication key for API access control
        - cputemp (str): File path for CPU temperature readings
        - logfilepath (str): Path to application log file
        - gunicornpath (str): Base directory for Gunicorn log files

Note:
    This module is a central configuration point for the application and should
    be imported by other modules that need access to global settings or version
    information.

"""

import random
import json
from base64 import b64decode, b64encode
from datetime import datetime

VERSION = '1.4.1'
API_KEY=''

def initialise():
    """Setup the settings dict structure with default values"""
    isettings = {'LastSave': '01/01/2000 00:00:01',
                 'api-key': 'Y2hhbmdlLW1l',
                 'oled_enabled': False,
                 'oled_address': 0x3C,
                 'oled_height': 64,
                 'oled_width': 128,
                 'app-name': 'Oxide Line Valve Controller',
                 'cputemp': '/sys/class/thermal/thermal_zone0/temp',
                 'gunicornpath': './logs/',
                 'logappname': 'Valve-Controller-Py',
                 'logfilepath': './logs/valvecontroller.log',
                 'loglevel': 'INFO',
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
                         'excluded': '0'
                     },
                     '2': {
                         'name': 'Ar tank pipette input',
                         'gpio': 22,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '3'
                     },
                     '3': {
                         'name': 'Ar tank pipette output',
                         'gpio': 27,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '2'
                     },
                     '4': {
                         'name': 'Ne tank pipette input',
                         'gpio': 18,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '5'
                     },
                     '5': {
                         'name': 'Ne tank pipette output',
                         'gpio': 17,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '4'
                     },
                     '6': {
                         'name': '4He Q tank pipette input',
                         'gpio': 13,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '7'
                     },
                     '7': {
                         'name': '4He Q tank pipette output',
                         'gpio': 12,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '6'
                     },
                     '8': {
                         'name': '3He spike tank pipette input',
                         'gpio': 11,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '9'
                     },
                     '9': {
                         'name': '3He spike tank pipette output',
                         'gpio': 9,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '8'
                     },
                     '10': {
                         'name': 'turbo to cryotrap',
                         'gpio': 24,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '11': {
                         'name': 'input to manifold',
                         'gpio': 21,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '12': {
                         'name': 'turbo to manifold',
                         'gpio': 20,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '13': {
                         'name': 'SRS RGA',
                         'gpio': 26,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '14': {
                         'name': 'cold getter',
                         'gpio': 16,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '15': {
                         'name': 'ion pump',
                         'gpio': 19,
                         'direction': 'output',
                         'enabled': True,
                         'excluded': '0'
                     },
                     '16': {
                         'name': 'Not Configured',
                         'gpio': 25,
                         'direction': 'input',
                         'enabled': False,
                         'excluded': '0'
                     }
                 },
                 'analogue_prefix': 'analogue',
                 'analogue_installed': False,
                 'analogue_i2c': 0x48,
                 'analogue_channels': {
                     '1': {
                         'name': 'Analogue 1',
                         'pin': 0,
                         'enabled': False
                     },
                     '2': {
                         'name': 'Analogue 2',
                         'pin': 1,
                         'enabled': False
                     },
                     '3': {
                         'name': 'Analogue 3',
                         'pin': 2,
                         'enabled': False
                     },
                     '4': {
                         'name': 'Analogue 4',
                         'pin': 3,
                         'enabled': False
                     }
                 },
                 'serial_channels': [
                     {"api-name": "ion-pump",
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
    return isettings


def generate_api_key(key_len):
    """generate a new random api-key"""
    allowed_characters = "ABCDEFGHJKLMNPQRSTUVWXYZ-+~abcdefghijkmnopqrstuvwxyz123456789"
    return ''.join(random.choice(allowed_characters) for _ in range(key_len))


def writesettings():
    """Write settings to a json file"""
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

def loadsettings():
    """Replace the default settings with those from the json files, if a setting is not in the json file (e.g. it is a
     new feature setting) then retain the default value and write that to the json file. If the api-key is the default
    value then generate a new key and save it."""
    global settings, API_KEY
    settingschanged = False
    fsettings = readsettings()
    for item in settings.keys():
        try:
            settings[item] = fsettings[item]
        except KeyError:
            print('settings[%s] Not found in json file using default' % item)
            settingschanged = True
    API_KEY = b64decode(settings['api-key']).decode('utf-8')
    if API_KEY == 'change-me':  # the default value
        settings['api-key'] = b64encode(generate_api_key(128).encode('utf-8')).decode('utf-8')
        API_KEY = b64decode(settings['api-key']).decode('utf-8')
        settingschanged = True
    if settingschanged:
        writesettings()

def friendlyname(sourcename: str) -> str:
    """
    Replaces invalid characters in a string with hyphens to create a valid
    friendly file file or host name. Invalid characters include file system restricted
    characters such as '/', '\', ':', '*', '?', '<', '>', '"', '&', '%', '#', '$',
    "'", ',' and '.', which could cause issues in file or directory names. Multiple
    replacement hyphens caused due to consecutive invalid characters are also
    collapsed to a single hyphen. Spaces are also removed to allow this function to generate hostnames.

    :param sourcename: A string containing the original directory name, which
        potentially includes invalid characters that need to be replaced.
    :type sourcename: str

    :return: A sanitized directory name with invalid characters replaced and
        multiple hyphens collapsed into one.
    :rtype: str
    """
    if len(sourcename) == 0:
        return ''
    invalid_chars = ['/', '\\', ':', '*', '?', '<', '>', '"', '&', '%', '#', '$', "'", ',', '.', ' ']
    for invalid_char in invalid_chars:
        sourcename = sourcename.replace(invalid_char, '-')
    # Remove double dash characters
    while '--' in sourcename:
        sourcename = sourcename.replace('--', '-')
    # Remove leading or training -
    if sourcename[0] == '-':
        sourcename = sourcename[1:]
    if sourcename[-1] == '-':
        sourcename = sourcename[:-1]
    return sourcename.lower()

def jscriptname(sourcename: str) -> str:
    """
    Processes a source name string by removing invalid characters and converting it
    to lowercase. This function ensures the input string conforms to a format
    suitable for use in contexts where certain characters are not allowed.

    :param sourcename: Input string to be processed. It may contain
        potentially invalid characters.
    :type sourcename: str
    :return: A clean and lowercase version of the input string with invalid
        characters removed.
    :rtype: str
    """
    if len(sourcename) == 0:
        return ''
    invalid_chars = ['/', '\\', ':', '-', '*', '?', '<', '>', '"', '&', '%', '#', '$', "'", ',', '.', ' ']
    for invalid_char in invalid_chars:
        sourcename = sourcename.replace(invalid_char, '')
    return sourcename.lower()

settings = initialise()
loadsettings()
