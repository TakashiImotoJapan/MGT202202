#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi
import MySQLdb

print('Content-type: text/html; charset=UTF-8\r\n')

form = cgi.FieldStorage()
text = form.getvalue('key','')
connection = MySQLdb.connect(host='172.16.200.11', user='test', passwd='test', db='testdb', charset='utf8')
cursor = connection.cursor()

cursor.execute("select * from user where username = '%s'" % (text))

print("""<!doctype html><html><head><title> test page. </title><body>""")
print("""<h1>search key: %s</h1>""" % (text))
print("""<table border="1">""")
for row in cursor.fetchall():
        print("""<tr><td>%s</td><td>%s</td></tr>""" % (row[1], row[2]))
print("""</table></body></html>""")
