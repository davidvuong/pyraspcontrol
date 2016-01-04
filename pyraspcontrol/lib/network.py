#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import urllib2
import subprocess

from subprocess import Popen
from datetime import datetime
from datetime import timedelta

from pyraspcontrol.lib import constants

_MAX_CONNECTIONS = 50
_INTERFACE = 'eth0'
_IP_SERVICE = 'http://ipecho.net/plain'
_IP_CACHE = {}


def _get_connections():
    ps = Popen(['netstat', '-nta'], stdout=subprocess.PIPE)
    ps = Popen(['wc', '-l'], stdin=ps.stdout, stdout=subprocess.PIPE)
    return int(ps.communicate()[0]) - 2


def _format_raw_usage(usage):
    return usage.replace('(', '').replace(')', '')


def _get_network_usage():
    ps = Popen(['/sbin/ifconfig', _INTERFACE], stdout=subprocess.PIPE)
    ps = Popen(['grep', 'RX\ bytes'], stdin=ps.stdout, stdout=subprocess.PIPE)
    network_usage = ps.communicate()[0]

    network_usage = network_usage.strip()
    network_usage = network_usage.replace('RX bytes:', '')
    network_usage = network_usage.replace('TX bytes:', '')
    return network_usage or None


def get_network_info():
    network_usage = _get_network_usage()
    if not network_usage:
        response = copy.deepcopy(constants.DEFAULT_ERROR_RESPONSE)
        response.update({'connections_alert': constants.DANGER})
        return response

    # RX Bytes: The number of bytes received (downloaded).
    # TX Bytes: The number of bytes transmitted (uploaded).
    #
    # A network interface is the point of interconnection between a computer and
    # a private or public network.
    #
    # https://en.wikipedia.org/wiki/Network_interface
    #
    # In our case, we are looking at information on the `_INTERFACE` (eth0)
    # interface.
    rx, tx = network_usage.split('  ')

    rx_bytes, rx_raw = rx.split(' ', 1)
    tx_bytes, tx_raw = tx.split(' ', 1)

    data = {
        'connections': _get_connections(),
        'up': int(rx_bytes),
        'down': int(tx_bytes),
        'rx_raw': _format_raw_usage(rx_raw),
        'tx_raw': _format_raw_usage(tx_raw),

        'connections_alert': constants.SUCCESS,
    }
    if data['connections'] > _MAX_CONNECTIONS:
        data['connections_alert'] = constants.WARNING
    return data


def get_internal_ip(request):
    return request.remote_addr


def get_external_ip():
    diff = datetime.now() - timedelta(minutes=1)
    if _IP_CACHE and _IP_CACHE['cached_at'] < diff:
        return _IP_CACHE['ip']

    try:
        external_ip = urllib2.urlopen(_IP_SERVICE).read()
        _IP_CACHE['ip'] = external_ip
        _IP_CACHE['cached_at'] = datetime.now()

        return external_ip
    except urllib2.HTTPError:
        return None
