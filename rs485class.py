"""
RS485 reader class, uses pyserial to read instrumentation data
"""
from time import sleep
from threading import Timer
import serial  # from pyserial
from logmanager import logger


class Rs485class:
    """Rs485Class reads data strings via RS85 port"""
    def __init__(self, port, speed, interval, readlength, readings):
        self.port = serial.Serial()
        self.port.port = port
        self.port.baudrate = speed
        self.interval = interval
        self.readings = readings
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

        except serial.serialutil.SerialException:
            logger.error("RS485Class: error opening port %s", port)
            timerthread = Timer(1, self.rs485_reader)
            timerthread.name = 'RS422 %s' % port
            timerthread.start()



    def rs485_reader(self):
        """Reads the serial port"""
        while True:
            try:
                if self.portready == 1:
                    self.port.reset_input_buffer()
                    databack = str(self.port.read(size=self.readlength), 'utf-8')
                    self.data = []
                    for item in self.readings:
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
