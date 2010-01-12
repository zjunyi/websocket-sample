#!/usr/bin/python
# -*- coding: utf-8 -*-

from mod_python import apache
import MeCab
import sys
import string
import urllib
import cgi
import re

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
				if re.match(u"^[ぁ-ん]*[ァ-ヴ]*[一-龠]+[ぁ-ん]*[ァ-ヴ]*$", m.surface.decode('utf-8')):
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

#def handler(req):
#	req.content_type = 'text/plain;charset=utf-8'
	
#	req.write("Hello, World!!")
	
#	return apache.OK

def answer(req, sentence):
	req.content_type = 'application/json;charset=utf-8'
	w = AutoRuby()
	
	out = w.run(sentence)
	
	return out

