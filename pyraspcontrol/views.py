#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import render_template
from pyraspcontrol.app import app
from pyraspcontrol.lib.uptime import get_uptime

from pyraspcontrol.lib.cpu import get_cpu_info
from pyraspcontrol.lib.cpu import get_temperature
from pyraspcontrol.lib.memory import get_ram_info
from pyraspcontrol.lib.memory import get_swap_info
from pyraspcontrol.lib.storage import get_disks


@app.route('/', methods=['GET'])
def index():
    context = {
        'page': 'index',
        'uptime': get_uptime(),
        'cpu': get_cpu_info(),
        'cpu_temp': get_temperature(),
        'ram': get_ram_info(),
        'swap': get_swap_info(),
        'storage': get_disks(),
    }
    return render_template('home.html', **context)


@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html', page='services')
