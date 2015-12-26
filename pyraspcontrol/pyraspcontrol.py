#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import flask

app = flask.Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('home.html', page='index')


@app.route('/details', methods=['GET'])
def details():
    return flask.render_template('details.html', page='details')


@app.route('/services', methods=['GET'])
def services():
    return flask.render_template('services.html', page='services')


@app.route('/disks', methods=['GET'])
def disks():
    return flask.render_template('disks.html', page='disks')

if __name__ == '__main__':
    app.run(port=8080)
