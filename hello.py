#!/usr/bin/env python3
import os
import json
import sys

#text/html might be useful for later
#print('Content-Type: application/json')
#print() #blank line seperates headers from content
#print(json.dumps(dict(os.environ), indent=2))
def login_page():
    """
    Returns the HTML for the login page.
    """

    return (r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)
   
print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
""")
print(login_page())
#for parameter in os.environ['QUERY_STRING'].split('&'):
#    (name, value) = parameter.split('=')
#    print(f"<li><em>{name}</em> = {value}</li>")
print("""
</body>
</html>""")    


posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")


#mdn form

#print('Content-Type: text/plain')
#print()
#print("Hello Browser!!!!")
