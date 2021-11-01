#!/usr/bin/env python

import socket

hostname = socket.getfqdn()

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return_string = "Hello World from", hostname
    return [list(return_string)]