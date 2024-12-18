"""
Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will creat from the defaults in the initialise function.
"""
import random
import json
from datetime import datetime

VERSION = '1.1.2'

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
                 'ion-length': 16,
                 'ion-port': '/dev/ttyUSB1',
                 'ion-speed': 9600,
                 'ion-start': 9,
                 'ion-string1': 'fiAwNSAwQiAwMA0=',  # base64 encoded
                 'ion-units': 'mbar',
                 'turbo-length': 16,
                 'turbo-port': '/dev/ttyUSB0',
                 'turbo-speed': 9600,
                 'turbo-start': 5,
                 'turbo-string1': 'UFIxDQ==',  # base64 encoded
                 'turbo-string2': 'BQ==',  # base64 encoded
                 'turbo-units': 'mbar',
                 }
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
        settings['api-key'] = generate_api_key(30)
        settingschanged = True
    if settingschanged:
        writesettings()


settings = initialise()
loadsettings()
