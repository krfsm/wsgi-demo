#!/usr/bin/env python

import socket

hostname = socket.getfqdn()

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World from" + hostname]