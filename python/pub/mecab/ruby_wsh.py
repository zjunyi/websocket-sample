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
class AutoRuby():
	def __init__(self):
		self.t = MeCab.Tagger ("")
	
	def run(self, sentence):
		ret = ''
		try:
			
			m = self.t.parseToNode (sentence)
			m = m.next
			while m:
				arr = m.feature.split(",")
				if len(arr) > 7:
					r = arr[7]
				else:
					r = ''
#				if (ret != ''):
#					ret += ' '

				# ひらがなかカタカナの時
				if re.match(u"^[ぁ-ん]*[ァ-ヴ]*[一-龠]+[ぁ-ん]*[ァ-ヴ]*[一-龠]*[ぁ-ん]*[ァ-ヴ]*$", m.surface.decode('utf-8')):
					ret += "<ruby>"+ m.surface + "<rp>(</rp><rt>" + r + "</rt><rp>)</rp></ruby>"
				else:
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
	w = AutoRuby()
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


