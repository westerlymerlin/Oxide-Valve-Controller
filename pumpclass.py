"""
Pump reader class, uses pyserial to read pressure gauges and pyrometer
"""
from time import sleep
from threading import Timer
from base64 import b64decode
import serial  # from pyserial
from logmanager import logger


class PumpClass:
    """PumpClass: reads pressures from gauges via RS232 ports"""
    def __init__(self, name, port, speed, start, length, string1=None, string2=None):
        self.name = name
        self.port = serial.Serial()
        self.port.port = port
        self.port.baudrate = speed
        self.start = start
        self.length = length
        self.port.parity = serial.PARITY_NONE
        self.port.stopbits = serial.STOPBITS_ONE
        self.port.bytesize = serial.EIGHTBITS
        # self.port.set_buffer_size(4096, 4096)
        self.port.timeout = 1
        self.value = 0
        self.portready = 0
        if string1 is None:
            self.string1 = None
        else:
            self.string1 = b64decode(string1)
        if string2 is None:
            self.string2 = None
        else:
            self.string2 = b64decode(string2)
        logger.info('Initialising %s pump on port %s', self.name, self.port.port)
        try:
            self.port.close()
            self.port.open()
            logger.info("%s port %s ok", self.name, self.port.port)
            self.portready = 1
            timerthread = Timer(1, self.serialreader)
            timerthread.name = self.name
            timerthread.start()
        except serial.serialutil.SerialException:
            logger.error("pumpClass error %s opening port %s", self.name, self.port.port)

    def serialreader(self):
        """Reads the serial port"""
        while True:
            try:
                if self.portready == 1:
                    if self.string1:
                        self.port.write(self.string1)
                        sleep(0.5)
                    if self.string2:
                        self.port.write(self.string2)
                    databack = self.port.read(size=100)
                    self.value = str(databack, 'utf-8')[self.start:self.length]
                    logger.info('Pump Return "%s" from %s', self.value, self.name)
                else:
                    self.value = 0
            except:
                logger.exception('Pump Error on %s: %s', self.name, Exception)
                self.value = 0
            sleep(5)

    def read(self):
        """Return the gauge pressure"""
        if self.value == '':
            return 0
        try:
            return float(self.value)
        except:
            return 0
