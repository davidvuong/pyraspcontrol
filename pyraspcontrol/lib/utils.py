#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read(file_):
    try:
        with open(file_, 'rU') as f:
            return f.read()
    except IOError:
        return None
