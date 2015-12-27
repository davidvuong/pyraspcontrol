#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyraspcontrol.app import app as application
from pyraspcontrol.views import *


if __name__ == '__main__':
    application.run(port=8080)
