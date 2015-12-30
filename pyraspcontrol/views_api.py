#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify
from pyraspcontrol.app import app
from pyraspcontrol.lib.network import get_external_ip


@app.route('/api/network-ip', methods=['GET'])
def get_network_ip():
    return jsonify(ip=get_external_ip())
