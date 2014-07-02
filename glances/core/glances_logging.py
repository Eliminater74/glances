# -*- coding: utf-8 -*-
#
# This file is part of Glances.
#
# Copyright (C) 2014 Nicolargo <nicolas@nicolargo.com>
#
# Glances is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Glances is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Custom logging class"""

import logging
import logging.config

# Define the logging configuration
LOGGING_CFG = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['file', 'console']
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s -- %(levelname)s -- %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': '/tmp/glances.log'
        },
        'console':{
            'level':'CRITICAL',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'debug': {
            'handlers':['file', 'console'],
            'level':'DEBUG',
        },
        'verbose': {
            'handlers': ['file', 'console'],
            'level': 'INFO'
        },
        'standard': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    }
}

def glancesLogger():
    _logger = logging.getLogger()
    logging.config.dictConfig(LOGGING_CFG)
    return _logger
