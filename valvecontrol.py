"""
Core valve control system interface module.

Provides hardware abstraction layer for valve monitoring and control operations:
- Real-time valve status monitoring and state management
- HTTP endpoint status checking and response handling
- Control command validation and execution
- System status reporting and error handling

All external valve interactions should go through this module to ensure
consistent state management and proper error handling. Implements thread-safe
operations for concurrent access.
"""

from threading import Timer
import os
from RPi import GPIO
from logmanager import logger
from app_control import settings, updatesetting
from pumpclass import PumpClass
from rs485class import Rs485class


logger.info('Application starting')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
channellist = [23, 22, 27, 18, 17, 13, 12, 11, 9, 24, 21, 20, 26, 16, 19]
GPIO.setup(channellist, GPIO.OUT)
GPIO.output(channellist, 0)

valves = [
    {
        'id': 1,
        'gpio': channellist[0],
        'description': 'heating cell',
        'excluded': 0
    },
    {
        'id': 2,
        'gpio': channellist[1],
        'description': 'Ar tank pipette input',
        'excluded': 3
    },
    {
        'id': 3,
        'gpio': channellist[2],
        'description': 'Ar tank pipette output',
        'excluded': 2
    },
    {
        'id': 4,
        'gpio': channellist[3],
        'description': 'Ne tank pipette input',
        'excluded': 5
    },
    {
        'id': 5,
        'gpio': channellist[4],
        'description': 'Ne tank pipette output',
        'excluded': 4
    },
    {
        'id': 6,
        'gpio': channellist[5],
        'description': '4He Q tank pipette input',
        'excluded': 7
    },
    {
        'id': 7,
        'gpio': channellist[6],
        'description': '4He Q tank pipette output',
        'excluded': 6
    },
    {
        'id': 8,
        'gpio': channellist[7],
        'description': '3He spike tank pipette input',
        'excluded': 9
    },
    {
        'id': 9,
        'gpio': channellist[8],
        'description': '3He spike tank pipette output',
        'excluded': 8
    },
    {
        'id': 10,
        'gpio': channellist[9],
        'description': 'turbo to cryotrap',
        'excluded': 0
    },
    {
        'id': 11,
        'gpio': channellist[10],
        'description': 'input to manifold',
        'excluded': 0
    },
    {
        'id': 12,
        'gpio': channellist[11],
        'description': 'turbo to manifold',
        'excluded': 0
    },
    {
        'id': 13,
        'gpio': channellist[12],
        'description': 'SRS RGA',
        'excluded': 0
    },
    {
        'id': 14,
        'gpio': channellist[13],
        'description': 'Ion Pump',
        'excluded': 0
    },
    {
        'id': 15,
        'gpio': channellist[14],
        'description': 'spare',
        'excluded': 0
    }
]


def parsecontrol(item, command):
    """Parser that recieves messages from the API or web page posts and directs
    messages to the correct function"""
    # print('%s : %s' % (item, command))
    try:
        if item == 'valvestatus':
            return valvestatus()
        if item[:5] == 'valve':
            valve = int(item[5:])
            if 0 < valve < 16:
                if command == 'open':
                    valveopen(valve)
                elif command == 'close':
                    valveclose(valve)
                else:
                    logger.warning('bad valve command')
            else:
                logger.warning('bad valve number')
            return valvestatus()
        if item == 'closeallvalves':
            allclose()
            return valvestatus()
        if item == 'getpressures':
            return pressures()
        if item == 'updatesetting':
            logger.warning('parsecontrol Setting changed via api - %s', command)
            updatesetting(command)
            return settings
        if item == 'getsettings':
            return settings
        if item == 'ion-debug':
            ionpump.commsdebug = command
            return {'status': 'ion-debug set to %s' % command}
        if item == 'restart':
            if command == 'pi':
                logger.warning('Restart command recieved: system will restart in 15 seconds')
                timerthread = Timer(15, reboot)
                timerthread.start()
            return {'status': 'rebooting'}
        return {'status': 'bad request'}
    except ValueError:
        logger.warning('incorrect json message')
        return {'status': 'incorrect json message'}
    except IndexError:
        logger.warning('bad valve number')
        return {'status': 'bad valve number'}


def valveopen(valveid):
    """Open the valve specified"""
    valve = [valve for valve in valves if valve['id'] == valveid]
    print(valve)
    if valve[0]['excluded'] > 0 and GPIO.input([valvex for valvex in valves if valvex['id'] == valve[0]['excluded']][0]['gpio']) == 1:
        logger.warning('cannot open valve as the excluded one is also open valve %s', valveid)
    else:
        GPIO.output(valve[0]['gpio'], 1)
        logger.info('Valve %s opened', valveid)


def valveclose(valveid):
    """Close the valve specified"""
    valve = [valve for valve in valves if valve['id'] == valveid]
    GPIO.output(valve[0]['gpio'], 0)
    logger.info('Valve %s closed', valveid)


def allclose():
    """Close all valves"""
    GPIO.output(channellist, 0)
    logger.info('All Valves Closed')


def status(value):
    """Meaningful value name for the specified valve"""
    if value == 0:
        return 'closed'
    return 'open'

def valvestatus():
    """Return the status of all valves as a jason message"""
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'valve': valve['id'], 'status': status(GPIO.input(valve['gpio']))})
    return statuslist




def httpstatus():
    """Status message formetted for the web status page"""
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'id': valve['id'], 'description': valve['description'],
                               'status': status(GPIO.input(valve['gpio']))})
    return statuslist

def statusmessage():
    """Return the status of all valves as a jason message"""
    statuslist = {}
    for valve in valves:
        if valve['id'] > 0:
            statuslist['valve%s' % valve['id']] = status(GPIO.input(valve['gpio']))
    if turbopump.portready == 0:
        turbovalue = 'Port not available'
    elif not turbopump.read():
        turbovalue = 'No Data Returned'
    else:
        turbodata = get_turbo_gauge_pressure()
        turbovalue = '%.4E (%s)' % (turbodata['turbo'], turbodata['turbounits'])
    if ionpump.portready == 0:
        ionvalue = 'Port not available'
    elif ionpump.value == '':
        ionvalue = 'Pump not connected'
    else:
        ionvalue = '%.4E (%s)' % (ionpump.read(), settings['ion-units'])
    statuslist['turbo'] = turbovalue
    statuslist['ion'] = ionvalue
    return statuslist



def reboot():
    """API call to reboot the Raspberry Pi"""
    logger.warning('System is restarting now')
    os.system('sudo reboot')


def get_turbo_gauge_pressure():
    """API call: return the turbo gauge pressure as a JSON message."""

    def calculate_turbo_pressure(value):
        """Calculate the turbo gauge pressure based on the value string."""
        base_pressure = float(value[:4]) / 1000
        exponent = int(value[4:]) - 20
        return base_pressure * (10 ** exponent)

    # Extract relevant pressure data
    pressure_data = next(
        (item for item in turbopump.read() if item['name'] == 'Turbo Gauge Pressure'),
        None
    )

    if pressure_data:
        turbo_pressure_value = calculate_turbo_pressure(pressure_data['value'])
        turbo_pressure_units = pressure_data['units']
        return {'turbo': turbo_pressure_value, 'turbounits': turbo_pressure_units}
    return {}


def pressures():
    """API call: return all guage pressures as a json message"""
    turbodata = get_turbo_gauge_pressure()
    pressure = [{'pump': 'turbo', 'pressure': turbodata['turbo'], 'units': turbodata['turbounits']},
                {'pump': 'ion', 'pressure': ionpump.read(), 'units': settings['ion-units']}]
    return pressure


def http_pump():
    """Web page info"""
    if turbopump.portready == 0:
        turbovalue = 'Port not available'
        turbounits = ''
    elif not turbopump.read():
        turbovalue = 'No Data Returned'
        turbounits = ''
    else:
        turbodata = get_turbo_gauge_pressure()
        turbovalue = '%.4E' % turbodata['turbo']
        turbounits = '(%s)' % turbodata['turbounits']
    if ionpump.portready == 0:
        ionvalue = 'Port not available'
        ionunits = ''
    elif ionpump.value == '':
        ionvalue = 'Pump not connected'
        ionunits = ''
    else:
        ionvalue = ionpump.value
        ionunits = '(%s)' % settings['ion-units']
    return [{'pump': 'turbo', 'pressure': turbovalue, 'units': turbounits},
                {'pump': 'ion', 'pressure': ionvalue, 'units': ionunits}]



turbopump = Rs485class(settings['RS485-port'], settings['RS485-speed'], settings['RS485-interval'],
                       settings['RS485-readlength'], settings['RS485-readings'])
ionpump = PumpClass('Ion Pump', settings['ion-port'], settings['ion-speed'], settings['ion-start'],
                    settings['ion-length'], settings['ion-string'])

logger.info('Application ready')
