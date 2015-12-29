#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from subprocess import check_output
from subprocess import CalledProcessError

from pyraspcontrol.lib import constants


def get_uptime():
    """Retrieves the uptime as a human-friendly (readable) string."""
    try:
        raw_uptime = check_output(['cat', '/proc/uptime'])
    except CalledProcessError:
        return {'uptime': 'N/A', 'alert': constants.DANGER}

    # `/proc/uptime`:
    #
    # The first number is the total number of seconds the system has been up. The
    # second number is how much of that time the machine has spent idle, in seconds.
    uptime, _ = raw_uptime.split(' ')

    # This uptime formatting is a copy of htop.
    #
    # https://github.com/hishamhm/htop/blob/0e8a02367ec7ca8f52b10de70938dfd07faed3ab/UptimeMeter.c
    total_seconds = int(math.ceil(float(uptime)))

    seconds = total_seconds % 60
    minutes = total_seconds / 60 % 60
    hours = total_seconds / 3600 % 24
    days = total_seconds / 86400

    days_str = ''
    if days > 100:
        days_str = '%d days(!), ' % days
    elif days > 1:
        days_str = '%d days, ' % days
    elif days == 1:
        days_str = '1 day, '
    return {
        'uptime': '%s%02d:%02d:%02d' % (days_str, hours, minutes, seconds),
        'alert': constants.SUCCESS if days < 100 else constants.WARNING
    }
