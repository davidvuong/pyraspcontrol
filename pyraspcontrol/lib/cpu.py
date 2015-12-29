#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import os
import multiprocessing

import subprocess
from subprocess import Popen

from pyraspcontrol.lib import utils
from pyraspcontrol.lib import constants

_MAX_TEMPERATURE = 85
_DANGER_TEMPERATURE_THRESHOLD = 80
_WARNING_TEMPERATURE_THRESHOLD = 60


def get_temperature():
    """Retrieves the Raspberry Pi's current CPU temperature.

    The temperature is taken directly from `/sys/class/thermal`. You can read more
    about it here: https://www.kernel.org/doc/Documentation/thermal/sysfs-api.txt

    A dictionary is returned containing the temperature in degrees (in Celsius),
    percentage (see `_MAX_TEMPERATURE`), and an alert status.

    Returns:
        dict: A dictionary of temperature related key value pairs.

    """
    temperature = utils.read('/sys/class/thermal/thermal_zone0/temp')
    temperature = int(temperature) / 1000
    data = {
        'degrees': temperature,
        'percentage': int(round(temperature / _MAX_TEMPERATURE)),
        'alert': constants.SUCCESS,
    }
    if data['percentage'] >= _DANGER_TEMPERATURE_THRESHOLD:
        data['alert'] = constants.DANGER
    if data['percentage'] >= _WARNING_TEMPERATURE_THRESHOLD:
        data['alert'] = constants.WARNING
    return data


def _execute_ps():
    # ps -e -o pcpu,user,args --sort=-pcpu | sed "/^ 0.0 /d" | head -5
    ps = Popen(['ps', '-e', '-o', 'pcpu,user,args', '--sort=-pcpu'], stdout=subprocess.PIPE)
    ps = Popen(['sed', '/^ 0.0 /d'], stdin=ps.stdout, stdout=subprocess.PIPE)
    ps = Popen(['head', '-' + constants.HEAD_LIMIT], stdin=ps.stdout, stdout=subprocess.PIPE)
    return ps.communicate()[0]


def get_cpu_info():
    """Retrieves additional CPU information on the Raspberry Pi."""
    data = {
        'loads': os.getloadavg(),  # 1, 5, 15 minutes.
        'cpu_count': multiprocessing.cpu_count(),
        'alert': constants.SUCCESS,
        'details': _execute_ps(),
        'cpu_data': {},
    }
    if data['loads'][0] > 1:
        data['alert'] = constants.DANGER

    cpu_data = data['cpu_data']
    for cpu_count in xrange(data['cpu_count']):
        i, cpu_data[cpu_count] = cpu_count, {}
        prefix = '/sys/devices/system/cpu/cpu%d/cpufreq/' % i

        freq = utils.read(prefix + 'scaling_cur_freq')
        cpu_data[i]['freq'] = int(freq) / 1000

        min_freq = utils.read(prefix + 'scaling_min_freq')
        cpu_data[i]['min_freq'] = int(min_freq) / 1000

        max_freq = utils.read(prefix + 'scaling_max_freq')
        cpu_data[i]['max_freq'] = int(max_freq) / 1000

        # https://wiki.archlinux.org/index.php/CPU_frequency_scaling#Scaling_governors
        cpu_data[i]['governor'] = utils.read(prefix + 'scaling_governor')
    return data
