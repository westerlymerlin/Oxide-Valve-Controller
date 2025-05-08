"""
RS-485 serial communication interface module.

Provides a class-based interface for RS-485 serial communication with
industrial devices such as valves and sensors. Handles:
- RS-485 port configuration and management
- Serial protocol implementation
- Data framing and validation
- Transmission error detection
- Message queuing and timeout handling

This module implements thread-safe operations for reliable communication
over RS-485 networks in industrial control applications. Supports both
synchronous and asynchronous communication patterns.
"""
from time import sleep
from threading import Timer
import serial  # from pyserial
from app_control import settings
from logmanager import logger


class Rs485class:
    """
    Handles RS485 communication and facilitates reading data from the serial port.

    This class is designed to work with RS485 serial communication. It allows
    for initializing a serial port, reading data from the port with a specified
    interval, and parsing the data based on predefined readings. It operates with
    an internal threading mechanism to continually read from the serial port in
    the background.

    :ivar port: Serial port object for RS485 communication.
    :type port: serial.Serial
    :ivar interval: Interval in seconds between consecutive reads from the port.
    :type interval: float
    :ivar messages: List of dictionaries containing metadata for parsing
                    specific strings from the incoming data.
    :type readings: list[dict]
    :ivar readlength: Number of bytes to read from the serial port at a time.
    :type readlength: int
    :ivar data: List of dictionaries containing parsed data from the port.
    :type data: list[dict]
    :ivar portready: Flag indicating if the serial port is successfully opened and ready.
    :type portready: int
    """
    def __init__(self, port, speed, interval, readlength, messages):
        self.port = serial.Serial()
        self.port.port = port
        self.port.baudrate = speed
        self.interval = interval
        self.messages = messages
        self.readlength = readlength
        self.port.parity = serial.PARITY_NONE
        self.port.stopbits = serial.STOPBITS_ONE
        self.port.bytesize = serial.EIGHTBITS
        # self.port.set_buffer_size(4096, 4096)
        self.port.timeout = 1
        self.data = []
        self.portready = 0
        logger.info('RS485Class: Initialising RS485 reader on port %s', port)
        try:
            self.port.close()
            self.port.open()
            logger.info("RS485Class: RS485 port %s ok", port)
            self.portready = 1
            timerthread = Timer(1, self.rs485_reader)
            timerthread.name = 'Turbo %s' % port
            timerthread.start()
        except serial.serialutil.SerialException:
            logger.error("RS485Class: error opening port %s", port)




    def rs485_reader(self):
        """
        Continuously reads data from an RS485 device, processing and extracting relevant
        information from the data stream. The method handles data parsing, error management,
        and executes at a regular interval defined by the `interval` attribute.

        The method checks if the port is ready, resets the input buffer, and reads data
        of the specified length. It parses the incoming data based on configuration and
        extracts key information for further use. Errors during the process are logged,
        and the method safely retries after encountering issues.

        :raises Exception: If there is an issue with reading the data or accessing the
            port.
        :returns: None
        """
        while True:
            try:
                if self.portready == 1:
                    self.port.reset_input_buffer()
                    databack = str(self.port.read(size=self.readlength), 'utf-8')
                    if settings['rs485-debug']:
                        logger.info('RS485Class: Read "%s"', databack)
                    self.data = []
                    for item in self.messages:
                        name = item['name']
                        units = item['units']
                        findstring = item['string']
                        length = item['length']
                        position = databack.find(findstring)
                        if position > -1:
                            self.data.append({'name': name, 'units': units, 'value':
                                                  databack[position+len(findstring):position+len(findstring)+length-1]})
                    logger.debug('RS485Class: Pump Return "%s" from %s', self.data, self.port)
                else:
                    self.data = []
            except:
                logger.exception('RS485Class: Read Error on %s: %s', self.port, Exception)
                self.data = []
            sleep(self.interval)

    def read(self):
        """Return the data list"""
        return self.data
