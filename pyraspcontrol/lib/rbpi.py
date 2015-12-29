#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""rbpi.py

This module provides general information such as the distribution, firmware, and
kernel for the Raspberry Pi.

"""
import flask
import socket
import subprocess

from subprocess import Popen
from subprocess import check_output


def get_distribution():
    ps = Popen(['cat', '/etc/os-release'], stdout=subprocess.PIPE)
    ps = Popen(['grep', 'PRETTY_NAME='], stdin=ps.stdout, stdout=subprocess.PIPE)

    distribution = ps.communicate()[0]
    distribution = distribution.replace('PRETTY_NAME=', '')
    distribution = distribution.replace('"', '')
    distribution = distribution.strip('\n')
    return distribution


def get_kernel():
    return check_output(['uname', '-mrs']).strip('\n')


def get_hostname():
    return socket.gethostname()


def get_webserver():
    return 'Flask %s' % flask.__version__
