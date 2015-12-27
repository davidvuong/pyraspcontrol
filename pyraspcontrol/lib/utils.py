#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read(file_):
    """Reads a file given the `file_` path and returns the content if exists."""
    try:
        with open(file_, 'rU') as f:
            return f.read()
    except IOError:
        return None
