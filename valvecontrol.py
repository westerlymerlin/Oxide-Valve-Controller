"""
Main valve controller module, operates the valves via the Raspberry Pi GPIO
"""

from threading import Timer
import os
from RPi import GPIO
from logmanager import logger
from app_control import settings
from pumpclass import PumpClass


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
        if item == 'restart':
            if command == 'pi':
                logger.warning('Restart command recieved: system will restart in 15 seconds')
                timerthread = Timer(15, reboot)
                timerthread.start()
            return {'status': 'rebooting'}
        return {'status': 'bad request'}
    except ValueError:
        logger.warning('incorrect json message')
    except IndexError:
        logger.warning('bad valve number')


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
    """Statud message formetted for the web status page"""
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'id': valve['id'], 'description': valve['description'],
                               'status': status(GPIO.input(valve['gpio']))})
    return statuslist


def reboot():
    """API call to reboot the Raspberry Pi"""
    logger.warning('System is restarting now')
    os.system('sudo reboot')

def pressures():
    """API call: return all guage pressures as a json message"""
    pressure = [{'pump': 'turbo', 'pressure': turbopump.read(), 'units': settings['turbo-units']},
                {'pump': 'ion', 'pressure': ionpump.read(), 'units': settings['ion-units']}]
    return pressure


def http_pump():
    """Web page info"""
    if turbopump.portready == 0:
        turbovalue = 'Port not available'
    elif turbopump.value == '':
        turbovalue = 'Pump not connected'
    else:
        turbovalue = turbopump.value
    if ionpump.portready == 0:
        ionvalue = 'Port not available'
    elif ionpump.value == '':
        ionvalue = 'Pump not connected'
    else:
        ionvalue = ionpump.value
    return [{'pump': 'turbo', 'pressure': turbovalue, 'units': settings['turbo-units']},
                {'pump': 'ion', 'pressure': ionvalue, 'units': settings['ion-units']}]



turbopump = PumpClass('Turbo Pump', settings['turbo-port'], settings['turbo-speed'], settings['turbo-start'],
                      settings['turbo-length'], settings['turbo-string1'], settings['turbo-string2'])
ionpump = PumpClass('Ion Pump', settings['ion-port'], settings['ion-speed'], settings['ion-start'],
                    settings['ion-length'], settings['ion-string1'])

logger.info('Application ready')
