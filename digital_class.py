"""
Raspberry Pi GPIO Digital I/O Control Module

This module provides a comprehensive interface for configuring and interacting with
Raspberry Pi GPIO pins. It abstracts the hardware-level details of GPIO operations
into a user-friendly class-based API, supporting both input and output operations.

Key features:
- ChannelObject class for configuring and interacting with individual GPIO channels
- Support for reading digital input values from GPIO pins
- Support for writing digital output values to GPIO pins
- Helper functions for checking digital key format and converting values
- System-wide digital channel initialization and management

The module integrates with the application's settings and logging systems to provide
consistent behavior and traceable operations across the entire application.

Dependencies:
    RPi.GPIO: For hardware-level GPIO control
    logmanager: For logging GPIO operations and errors
    app_control: For accessing application-wide settings
"""

from RPi import GPIO
from logmanager import logger
from app_control import settings

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class ChannelObject:
    """
    Represents a GPIO channel object for controlling and reading GPIO pins.

    This class provides functionality to configure a GPIO channel for input or
    output and read/write digital values. It also maintains details about the
    channel, such as its current state, direction, and description.
    """

    def __init__(self, channel_settings):
        """
        Initializes a new instance of the GPIO configuration class.

        This constructor sets up the configuration for a General Purpose Input/Output
        (GPIO) pin, including its pin number, direction, whether it is enabled, and
        additional descriptive attributes. These parameters define the behavior and
        the state of the GPIO pin.
        """
        self.gpio = channel_settings['gpio']
        self.direction = channel_settings['direction']
        self.enabled = channel_settings['enabled']
        self.name = channel_settings['name']
        self.excluded = channel_settings['excluded']
        if self.direction == 'input':
            GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        else:
            GPIO.setup(self.gpio, GPIO.OUT)

    def write(self, value):
        """
        Sets the digital channel to the specified value if it is enabled and configured
        as an output channel. The value controls the GPIO state based on predefined
        commands. Invalid values or improper configurations log warnings and result
        in no changes.

        :param value: The command to set the digital channel's GPIO (e.g., digital_on
                      or digital_off commands).
        :type value: str
        :return: The current state of the GPIO after attempting to set it, or -1 if
                 the operation fails due to a disabled channel, input configuration,
                 or invalid value.
        :rtype: int
        """
        if not self.enabled:
            logger.warning('Cannot set digital channel "%s" as it is disabled', self.name)
            return '', 'Cannot set digital channel %s as it is disabled' % self.name
        if self.direction != 'output':
            logger.warning('Cannot set digital channel "%s" as it is an input channel', self.name)
            return GPIO.input(self.gpio), 'Cannot set digital channel %s as it is an input channel' % self.name
        if value == settings['digital_on_command']:
            if int(self.excluded) > 0:
                if digital_channels[int(self.excluded)].read() == 1:
                    logger.warning('Cannot set digital channel "%s" as it is excluded partner is %s',
                                   self.name, digital_value(1))
                    return (GPIO.input(self.gpio), 'Cannot set digital channel %s as it is excluded partner is %s'
                            % (self.name, digital_value(1)))
            GPIO.output(self.gpio, 1)
        elif value == settings['digital_off_command']:
            GPIO.output(self.gpio, 0)
        else:
            logger.warning('Invalid value "%s" for digital channel "%s"', value, self.name)
            return GPIO.input(self.gpio), 'Invalid value %s for digital channel %s' % (value, self.name)
        logger.info('Digital Channel "%s" set to "%s"', self.name, value)
        return GPIO.input(self.gpio), ''

    def read(self):
        """
        Reads the current state of the GPIO pin.

        This method reads and returns the current logical state of the specified
        GPIO pin. It uses the GPIO library to retrieve the input value, which
        indicates whether the pin is logically HIGH or LOW.

        :return: Logical state of the GPIO pin as returned by the GPIO library
        :rtype: int or bool
        """
        return GPIO.input(self.gpio)


def check_digital_key(item):
    """
    Check if the given item matches a digital key based on a predefined prefix.

    This function iterates through a range of identifiers and checks if the
    provided item matches a specific format comprising a digital prefix and an
    identifier value. If a match is found, it returns True. Otherwise, it
    returns False.

    :param item: The item to be checked against the digital key format.
    :type item: str
    :return: A boolean indicating whether the given item matches the expected digital key format.
    :rtype: bool
    """
    for item_id in range(1, 17):
        if item == '%s%d' % (settings['digital_prefix'], item_id):
            return True
    return False


def digital_value(value):
    """
    Convert a digital input value to its corresponding system-defined digital representation.

    This function checks the given digital input value and returns the corresponding value
    from the system's settings. If the input value does not match predefined digital states,
    it will return 'error'.

    :param value: The digital input value to evaluate.
    :type value: int
    :return: The system-defined digital value corresponding to the input or 'error' if the input
             is invalid.
    :rtype: str
    """
    if value == 1:
        return settings['digital_on_value']
    if value == 0:
        return settings['digital_off_value']
    return 'error'


def digital_single_channel(item, command):
    """
    Executes a command to read or write the state of a single digital channel.

    This function processes the input channel and state, determines the operation
    to perform, and either reads the current channel state or updates the channel's
    state based on the provided command. The function then returns the updated or
    read channel state in a predefined format.
    """
    channel = int(item[len(settings['digital_prefix']):])
    if command not in [settings['digital_on_command'], settings['digital_off_command']]:
        ret_value = digital_channels[channel].read()
        errorvalue = ''
    else:
        ret_value, errorvalue = digital_channels[channel].write(command)
    if errorvalue != '':
        return {'item': item, 'command': command, 'exception': errorvalue, 'values':
            {'%s%d' % (settings['digital_prefix'], channel): {'value': digital_value(ret_value),
                                                              '%s' % settings['digital_prefix']: channel}}}
    return {'item': item, 'command': command, 'values': {'%s%d' % (settings['digital_prefix'], channel):
                                                             {'value': digital_value(ret_value),
                                                              '%s' % settings['digital_prefix']: channel}}}


def digital_all_values(item, command):
    """
    Generates a json representation of digital values for configured digital channels.

    This function iterates through a predefined range of digital channel IDs, retrieves
    their respective metadata and status, and returns a dictionary containing the
    digital channel attributes.

    :return: A dictionary representing the digital channels' values, where the keys
             are prefixed with the configured digital prefix, and the values contain
             the channel's ID, name, direction, status, and whether it is enabled.
    :rtype: dict
    """
    returned_data = {}
    for item_id in range(1, 17):
        returned_data['%s%d' % (settings['digital_prefix'], item_id)] = {'%s' % settings['digital_prefix']: item_id,
                                                                         'name': digital_channels[item_id].name,
                                                                         'direction': digital_channels[
                                                                             item_id].direction,
                                                                         'enabled': digital_channels[item_id].enabled,
                                                                         'value': digital_value(
                                                                             digital_channels[item_id].read())}
    return {'item': item, 'command': command, 'values': returned_data}


# setup digital channels
digital_channels = {}
for i in range(1, 17):
    digital_channels[i] = ChannelObject(settings['digital_channels'][str(i)])
