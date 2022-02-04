#!/usr/bin/env python

import json
import socket

hostname = socket.getfqdn()

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    if env['REQUEST_URI'] == '/api/getinspired.json':
        return_string = 'getinspiration.json requested'
    else:
        return_string = "Hello World from " + hostname
    return return_string.encode('utf-8')
