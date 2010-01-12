#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab
import sys
import string

class WakachiNoun():
	def __init__(self):
		self.t = MeCab.Tagger ("")
	
	def run(self, sentence):
		ret = ''
		try:
			
			m = self.t.parseToNode (sentence)
			m = m.next
			while m:
				h = m.feature.split(",")[0]
				if (h == '名詞'):
					if (ret != ''):
						ret += ' '
					ret += m.surface
				m = m.next

		except RuntimeError, e:
			ret = ''
		
		return ret

w = WakachiNoun()

print w.run(u'もももすももももものうち'.encode('utf_8'))
print w.run('昨日、神田でラーメンを食べた')
