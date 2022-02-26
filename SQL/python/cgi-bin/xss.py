#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import io
import cgi

import subprocess

import MySQLdb

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
text = form.getvalue('key','')
text = MySQLdb.escape_string(text).decode('utf-8')

del_id = form.getvalue('delkey','')

connection = MySQLdb.connect(host='172.16.200.11', user='test', passwd='test', db='testdb', charset='utf8')
cursor = connection.cursor()

if len(text) > 0:
    cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (text, "0123456789"))
    connection.commit()


if len(del_id) > 0:
    cursor.execute("DELETE FROM user WHERE id = %s", (del_id))
    connection.commit()

cursor.execute("select * from user")

print("Content-Type: text/html;charset=utf-8\n\n")
print("")
print("""<!DOCTYPE html><html><head><title> test page. </title></head><body>""")
print("""<h1>ユーザ登録: %s</h1>""" % (text))
print("""
        <form action="/cgi-bin/xss.py" method="post">
                <p>
                <input type="text" name="key" size="40">
                <input type="submit" value="登録">
                </p>
        </form>
""")
print("""<table>""")
for row in cursor.fetchall():
    print("""<tr><td>%s</td><td>
        <form action="/cgi-bin/xss.py" method="post">
            <input type="hidden" name="delkey" value="%s">
            <input type="submit" value="削除">
        </form>
    </td></tr>""" % (row[1], row[0]))
print("""</table>""")
print("""</body></html>""")

cursor.close()
connection.close()
