#!/usr/bin/env python

import argparse

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, jsonify
from subprocess import call
from services import screencontrol

BASE_URL = ''

app = Flask(__name__)


app.config['services'] = {
    "ScreenControl": screencontrol.ScreenControl()
}


@app.route("/")
@app.route("/<service>")
def index(service=None):
    # Get the services from the config file
    services = []
    for dev in app.config['services'].keys():
        d = {
            'id': dev,
            'name': dev,
        }
        services.append(d)
    
    return render_template('remote.html', services=services)


@app.route("/service/<service_id>")
def service(service_id=None):
    d = {'id':service_id,
         'keydefs': dict(app.config['services'][service_id])
         }
    if 'format' in request.args:
        print request.args['format']
        return jsonify(d)
    else:
        return render_template('control.html', d=d)


@app.route("/service/<service_id>/<op>")
def clicked(service_id=None, op=None):
    # Call the associated command

    if not dict(app.config['services'][service_id])[op]():
        return ""
    else:
        return ""



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ipaddr',
                        default="0.0.0.0",
                        help="IP address to listen on, default %(default)s")
    parser.add_argument('-p', '--port',
                        default=5000,
                        type=int,
                        help="Port to listen on, default %(default)s")
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug mode, default %(default)s")
    args = parser.parse_args()

    app.run(args.ipaddr, args.port, debug=args.debug)


