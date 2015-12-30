#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/var/www/pyraspcontrol')

from pyraspcontrol import config
from pyraspcontrol.app import app as application
from pyraspcontrol.views import *
from pyraspcontrol.views_api import *


if __name__ == '__main__':
    application.run(port=config.PORT)
