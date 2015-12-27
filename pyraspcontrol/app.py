#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask

app = flask.Flask(__name__)
app.config.from_object('pyraspcontrol.config')
