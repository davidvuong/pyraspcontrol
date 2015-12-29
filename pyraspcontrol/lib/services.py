#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from subprocess import check_output

_STATUS_TYPES = {
    '[ - ]': 'stopped',
    '[ + ]': 'running',
    '[ ? ]': 'unknown',
}


def get_services():
    """Retrieves all running, stopped, and unknown services on the Pi."""
    services = check_output(
        ['/usr/sbin/service', '--status-all'], stderr=subprocess.STDOUT
    ).strip('\n')

    # How to interpret service status:
    #
    # http://superuser.com/questions/367863/how-do-interpret-the-output-of-service-status-all
    data = []
    for service in services.split('\n'):
        status, name = service.strip().split('  ')
        data.append({
            'name': name.strip(),
            'status': _STATUS_TYPES[status],
        })
    return data


def get_service_info(service_name):
    """Given a `service_name`, retrieve detailed info on service as a string."""
    return check_output(['/usr/sbin/service', service_name, 'status']).strip('\n')
