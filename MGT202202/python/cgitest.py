#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi
import MySQLdb

form = cgi.FieldStorage()
text = form.getvalue('key','')
connection = MySQLdb.connect(host='127.0.0.1', user='test', passwd='test', db='testdb', charset='utf8')
cursor = connection.cursor()

cursor.execute("select * from user where username = '%s'" % (text))

print("""<!doctype html><html><head><title> test page. </title><body>""")
for row in cursor.fetchall():
	print(row)
print("""<h1>search key: %s</h1></body></html>""" % (text))
