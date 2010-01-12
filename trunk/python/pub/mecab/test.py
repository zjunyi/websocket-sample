#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

text = u'%E3%82%82%E3%82%82%E3%82%82'

sentence = urllib.unquote_plus(text).encode('raw_unicode_escape').decode('utf8')
#sentence = urllib.unquote_plus(text).encode('raw_unicode_escape')

print sentence
print type(sentence)
#encoded = urllib
print type(sentence.encode('utf_8'))

out = urllib.quote_plus(sentence.encode('utf_8'))

print out
