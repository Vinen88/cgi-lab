#!/usr/bin/env python3
import os
import json
import sys
import secret


posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    for line in posted.splitlines():
        values = line.split('&')
        usr = values[0].split('=')[1]
        passw = values[1].split('=')[1]
    if usr == secret.username and passw == secret.password:
        print('Set-Cookie: Loggedin=True')
print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
""")
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        values = line.split('&')
        usr = values[0].split('=')[1]
        passw = values[1].split('=')[1]
        print(line)
    print("</pre></p>")
    if usr == secret.username and passw == secret.password:
        print()

print("""
</body>
</html>""")  



#print('Content-Type: application/json')
#print() #blank line seperates headers from content
#print(json.dumps(dict(os.environ), indent=2))