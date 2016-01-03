#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify
from flask import render_template

from pyraspcontrol.app import app
from pyraspcontrol.lib.network import get_external_ip
from pyraspcontrol.lib.services import get_services


@app.route('/api/network-ip', methods=['GET'])
def get_network_ip():
    return jsonify(ip=get_external_ip())


@app.route('/api/services', methods=['GET'])
def list_services():
    services = get_services()
    return render_template('components/services.tpl.html', services=services)
