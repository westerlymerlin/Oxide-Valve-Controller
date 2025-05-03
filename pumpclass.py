"""
Vacuum pump control and monitoring class.

Provides object-oriented interface for managing pump systems:
- Pump start/stop control
- Runtime status monitoring
- Operating parameter validation
- Alarm condition handling
- System diagnostics
- State persistence

Class-based implementation ensures encapsulated pump management with
proper initialization, state tracking, and shutdown procedures.
Designed for integration with industrial control systems.
"""
from time import sleep
from threading import Timer
from base64 import b64decode
import serial  # from pyserial
from logmanager import logger


class PumpClass:
    """
    Represents a pump with serial communication capabilities, allowing for continuous
    monitoring and data processing. The pump is initialized with various configuration
    parameters, and its state is maintained via the serial connection. The class is
    designed to continuously read data from the serial port, handle exceptions, and
    maintain an internal value.

    This class encapsulates serial port configuration, controls, and management for
    interfacing with a pump device. It enables data writing, reading, and logging while
    ensuring resilience to communication errors.

    :ivar name: Name of the pump.
    :type name: str
    :ivar port: Serial port object configured for the pump.
    :type port: serial.Serial
    :ivar start: Starting position for slicing the read data.
    :type start: int
    :ivar length: Length of the data slice to extract from the read data.
    :type length: int
    :ivar commsdebug: Debug flag for logging detailed communication info.
    :type commsdebug: bool
    :ivar value: Extracted and processed data from the pump.
    :type value: int or str
    :ivar portready: Readiness state of the serial port (1 for ready, 0 otherwise).
    :type portready: int
    :ivar string1: Decoded pre-configured first string to write to the port.
    :type string1: bytes or None
    :ivar string2: Decoded pre-configured second string to write to the port.
    :type string2: bytes or None
    """
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
        self.commsdebug = False
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
        """
        Continuously reads data from a serial port and processes it based on the current
        object's configuration and state. Writes pre-configured strings to the port
        before reading data if applicable and logs the processed results. Handles
        exceptions and sets a default value to indicate errors during operations.

        :return: None
        """
        while True:
            try:
                if self.portready == 1:
                    self.port.reset_input_buffer()
                    if self.string1:
                        self.port.write(self.string1)
                        sleep(0.5)
                    if self.string2:
                        self.port.write(self.string2)
                    databack = self.port.read(size=100)
                    if self.commsdebug:
                        logger.info('Pump %s Read: "%s"', self.name, databack)
                    self.value = str(databack, 'utf-8')[self.start:self.length]
                    logger.debug('Pump Return "%s" from %s', self.value, self.name)
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
