#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_pywebsocket import msgutil
import sys
import string
import re
import base64

def getImage():
	img = open('/home/komasshu/websock_handler/pub/100images/dog.png', 'rt').read()
	
	data = 'data:image/png;base64,'+ base64.b64encode(img)
	
	return data

_HEATBEAT = 'Heartbeat'

def web_socket_do_extra_handshake(request):
#    if request.ws_origin != 'http://localhost':
#      raise "ws_origin error "+request.ws_origin
    pass  # Always accept.


def web_socket_transfer_data(request):
	data = getImage()
	while True:
		try:
			line = msgutil.receive_message(request).encode('utf-8')
			if line == _HEATBEAT:
				continue
		    
			if (line != ''):
				msgutil.send_message(request, data.decode('utf-8'))
		except Exception:
			return


