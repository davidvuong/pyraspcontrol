#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def read(file_):
    """Reads a file given the `file_` path and returns the content if exists."""
    try:
        with open(file_, 'rU') as f:
            return f.read()
    except IOError:
        return None


def strip_whitespace(string):
    """Strips all leading, trailing and in-between whitespaces.

    >>> strip_whitespace('hello  world  ')
    'hello world'
    >>> strip_whitespace(None)
    ''
    >>> strip_whitespace('')
    ''
    >>> strip_whitespace('hello world')
    'hello world'

    """
    return re.sub(r' +', ' ', string).strip() if string else ''
