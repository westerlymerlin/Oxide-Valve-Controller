"""
A module for managing custom API commands and parsing incoming commands.

This module defines a mechanism to handle custom commands that are listed in
the `custom_api` list. If the commands are unknown or errors are encountered
during the parsing process, appropriate error logging and responses are
generated.
"""

from logmanager import logger


custom_api = []

def custom_parser (item, command):
    """custom api commands, the items must be listed in the custom_api list for these to be called"""
    try:
        logger.warning('unknown item %s command %s', item, command)
        return {'error': 'unknown custom api command'}
    except ValueError:
        logger.error('Custom API Parser incorrect json message, value error')
        return {'error': 'bad value in json message custom api'}
    except IndexError:
        logger.error('Custom API Parser incorrect json message, index error')
        return {'error': 'Bad index in json message custom api'}
