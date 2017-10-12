#

import sys
from urllib.request import Request, urlopen
from datetime import *

try:
    url = 'http://localhost:8088/mysite3/guestBook/ajax'

    resp = urlopen(Request(url))
    resp_body = resp.read().decode('utf-8')
    print(resp_body)

except Exception as e:
    print("%s : %s" % (e, datetime.now()), file=sys.stderr)