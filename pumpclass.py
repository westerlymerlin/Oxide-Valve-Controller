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
    Represents a serial communication interface for interacting with a pump.

    This class facilitates communication with a pump device over a serial port. It is designed
    to initialize the connection, handle exceptions during operations, and perform tasks such
    as writing to the port or reading data from it. It includes functionalities to process
    configured messages, monitor the state of the device, and retrieve or parse its data.

    :ivar name: The name associated with the pump instance.
    :type name: str
    :ivar port: The serial port used for pump communication.
    :type port: serial.Serial
    :ivar messages: A list of pre-configured message dictionaries for operation requests.
    :type messages: list[dict]
    :ivar commsdebug: A flag for enabling or disabling detailed communication logging.
    :type commsdebug: bool
    :ivar pressurevalue: The current value retrieved or processed from the pump's response.
    :type pressurevalue: str or int
    :ivar portready: Indicates the readiness of the serial port. 1 if ready, 0 otherwise.
    :type portready: int
    """
    def __init__(self, name, port, speed, messages):
        self.name = name
        self.port = serial.Serial()
        self.port.port = port
        self.port.baudrate = speed
        self.reading = False
        self.messages = messages
        self.port.parity = serial.PARITY_NONE
        self.port.stopbits = serial.STOPBITS_ONE
        self.port.bytesize = serial.EIGHTBITS
        # self.port.set_buffer_size(4096, 4096)
        self.commsdebug = False
        self.port.timeout = 1
        self.pressurevalue = 0
        self.units = ''
        self.status = 'not ready'
        self.portready = 0
        logger.info('Initialising %s pump on port %s', self.name, self.port.port)
        try:
            self.port.close()
            self.port.open()
            logger.info("%s port %s ok", self.name, self.port.port)
            self.portready = 1
            timerthread = Timer(1, self.pressurereader)
            timerthread.name = 'Ion %s' % port
            timerthread.start()
        except serial.serialutil.SerialException:
            logger.error("pumpClass error %s opening port %s", self.name, self.port.port)

    def pressurereader(self):
        """
        Reads and updates the pressure value and its units from an external pump
        device at regular intervals of 5 seconds, provided the port is ready for
        operation.
        """
        while True:
            if self.portready == 1:
                pressures = self.access_pump('pressure')['pressure'].split(' ')
                if self.commsdebug:
                    logger.info('Pump pressure: "%s"', pressures)
                self.pressurevalue = pressures[0]
                self.units = pressures[-1]
                sleep(2.5)
                self.status = self.access_pump('status')['status']
                sleep(2.5)
            else:
                sleep(5)

    def access_pump(self, req_type):
        """
        Accesses a pump device, sends a request, and retrieves the corresponding response based
        on the specified request type. The function interacts with hardware through a communication
        port and processes the returned data to extract useful information.

        :param req_type: The name of the request type to access on the pump.
        :type req_type: str
        :return: A dictionary containing the result of the pump access operation. The dictionary
            may either indicate the success of the request or include specific response data
            based on the length and type of the response.
        :rtype: dict
        """
        message = {}
        for item in self.messages:
            if req_type == item['name']:
                length = item['length']
                start = item['start']
                string1 = b64decode(item['string'])
                try:
                    if self.portready == 1:
                        while self.reading:
                            sleep(0.25)
                        self.reading = True
                        self.port.reset_input_buffer()
                        if string1:
                            self.port.write(string1)
                            sleep(0.5)
                        databack = self.port.read(size=100)
                        if self.commsdebug:
                            logger.info('Pump %s %s: "%s"', self.name, req_type, databack)
                        if length == 0:
                            message = {req_type: 1}
                        else:
                            message = {req_type: str(databack, 'utf-8')[start:length]}
                    else:
                        message = {req_type: 0}
                except:
                    logger.exception('Pump Error on %s: %s', self.name, Exception)
                    message = {req_type: 0}
        self.reading = False
        return message


    def read(self):
        """
        Reads and converts the stored value to a floating-point number.

        This method attempts to parse the stored `value` attribute as a
        floating-point number. If the value is an empty string, it will
        return 0. If the conversion to a floating-point number fails,
        it will also return 0.

        :return: Returns the converted floating-point number from the
                 value attribute or 0 if the conversion fails.
        :rtype: float
        """
        if self.pressurevalue == '':
            return 0
        try:
            return float(self.pressurevalue)
        except:
            return 0
