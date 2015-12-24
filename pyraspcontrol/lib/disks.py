#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import shlex
from subprocess import check_output


def get_disks():
    disks = check_output(['lsblk', '--pair'])
    disks = disks.strip('\n').split('\n')

    data = []
    for disk in disks:
        d = {}
        for disk_data in shlex.split(disk):
            key, value = disk_data.split('=', 1)
            d[key.lower()] = value
        data.append(d)
    return data
