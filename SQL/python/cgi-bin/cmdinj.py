#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import io
import cgi
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
text = form.getvalue('key','')

cmd = "/home/python/cgi-bin/find.sh " + text

res = None
try:
    res = subprocess.check_output(cmd, shell=True)
except:
    a = 0

print("Content-Type: text/html;charset=utf-8\n\n")
print("")
print("""<!DOCTYPE html><html><head><title> test page. </title></head><body>""")
print("""<h1>res: %s</h1>""" % (res))
print("""<h1>検索ユーザ: %s</h1>""" % (text))
print("""
        <form action="/cgi-bin/cmdinj.py" method="post">
                <p>
                <input type="text" name="key" size="40">
                <input type="submit" value="送信">
                </p>
        </form>
""")
if res is None:
    print("ログインしていません。")
else:
    print("ログインしています。")
print("""</body></html>""")
