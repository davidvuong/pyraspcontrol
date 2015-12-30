#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request

from pyraspcontrol.app import app
from pyraspcontrol.lib.uptime import get_uptime

from pyraspcontrol.lib import rbpi
from pyraspcontrol.lib.cpu import get_cpu_info
from pyraspcontrol.lib.cpu import get_temperature
from pyraspcontrol.lib.memory import get_ram_info
from pyraspcontrol.lib.memory import get_swap_info
from pyraspcontrol.lib.storage import get_disks
from pyraspcontrol.lib.network import get_network_info
from pyraspcontrol.lib.network import get_internal_ip
from pyraspcontrol.lib.users import get_connected_users


def _get_context():
    return {
        'hostname': rbpi.get_hostname(),
        'kernel': rbpi.get_kernel(),
        'distribution': rbpi.get_distribution(),
        'webserver': rbpi.get_webserver(),
    }


@app.route('/', methods=['GET'])
def index():
    context = _get_context()
    context.update(**{
        'page': 'index',
        'uptime': get_uptime(),
        'cpu': get_cpu_info(),
        'cpu_temp': get_temperature(),
        'ram': get_ram_info(),
        'swap': get_swap_info(),
        'storage': get_disks(),
        'network': get_network_info(),
        'ip_internal': get_internal_ip(request),
        'connected_users': get_connected_users(),
    })
    return render_template('home.html', **context)


@app.route('/services', methods=['GET'])
def services():
    context = _get_context()
    context.update(**{
        'page': 'services',
    })
    return render_template('services.html', **context)
