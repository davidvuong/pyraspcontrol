#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from subprocess import check_output
from subprocess import Popen

from pyraspcontrol.lib.utils import strip_whitespace


def _clean_output(output):
    return strip_whitespace(output).strip('\n').split('\n')


def _execute_who(args):
    """Executing the `who` command to determine users logged into the Pi.

    Based on the options given, who can also list the user's name, terminal
    line, login time, elapsed time since activity occurred on the line, and
    the process ID of the command interpreter for each current system user.

    @see: http://pubs.opengroup.org/onlinepubs/009695399/utilities/who.html

    """
    return check_output(['who', '--' + args, '-a'])


def _get_connected_users():
    ps = Popen(['who', '-q'], stdout=subprocess.PIPE)
    ps = Popen(['grep', 'users='], stdin=ps.stdout, stdout=subprocess.PIPE)

    users = ps.communicate()[0]
    return int(users.split('users=')[-1])


def get_users():
    users, users_dns = _execute_who('ips'), _execute_who('lookup')

    dns_map = []
    for user in _clean_output(users_dns):
        user_info = user.split(' ')

        dns_map.append(
            user_info[-1] if len(user_info) == 5 else None
        )

    user_data = []
    for i, user in enumerate(_clean_output(users)):
        user_info = user.split(' ')
        user_data.append({
            'user': user_info[0],
            'login_at': '%s %s' % (user_info[2], user_info[3]),

        })
    return {'connected_users': _get_connected_users(), 'user_data': user_data}
