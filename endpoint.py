#!/usr/bin/env python

import json
import socket

hostname = socket.getfqdn()

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    print(env)
    if env['REQUEST_URI'] == '/api/endpoint.json':
        return_string = 'Endpoint.json requested'
    elif env['REQUEST_URI'] == '/api/login.json':
        return_string = 'This will be a login endpoint'
    else:
        return_string = "Hello World from " + hostname
    return return_string.encode('utf-8')
