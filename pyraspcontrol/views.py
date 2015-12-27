#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import render_template
from pyraspcontrol.app import app
from pyraspcontrol.lib.uptime import get_uptime


@app.route('/', methods=['GET'])
def index():
    context = {
        'page': 'index',
        'uptime': get_uptime(),
    }
    return render_template('home.html', **context)


@app.route('/details', methods=['GET'])
def details():
    return render_template('details.html', page='details')


@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html', page='services')


@app.route('/disks', methods=['GET'])
def disks():
    return render_template('disks.html', page='disks')
