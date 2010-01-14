#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_pywebsocket import msgutil
import MeCab
import sys
import string
import re

"""
This class "wakachi" given sentence only Noun.
"""
class Wakachi():
	def __init__(self):
		self.t = MeCab.Tagger ("")
	
	def run(self, sentence):
		ret = ''
		try:
			
			m = self.t.parseToNode (sentence)
			m = m.next
			while m:
				arr = m.feature.split(",")
				h = arr[0]
				if (ret != ''):
					ret += ' '

				# ひらがなかカタカナの時
#				if h == '名詞':
#					ret += m.surface+"("+h+")"
				ret += m.surface
					
				m = m.next

		except RuntimeError, e:
			ret = ''
		
		return ret

"""
w = WakachiNoun()

print w.run('もももすももももものうち')
print w.run('昨日、神田でラーメンを食べた')
"""

_HEATBEAT = 'Heartbeat'

def web_socket_do_extra_handshake(request):
#    if request.ws_origin != 'http://localhost':
#      raise "ws_origin error "+request.ws_origin
    pass  # Always accept.


def web_socket_transfer_data(request):
	w = Wakachi()
	while True:
		try:
			line = msgutil.receive_message(request).encode('utf-8')
			if line == _HEATBEAT:
				continue
		    
			if (line != ''):
				resp = w.run(line)
				msgutil.send_message(request, resp.decode('utf-8'))
		except Exception:
			return


