import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = 'http://localhost:8088/mysite3/api/guestBook/list'

    resp = urlopen(Request(url))
    resp_body = resp.read().decode('utf-8')
    json_result = json.loads(resp_body)

    print(json_result)
except Exception as e:
    print("%s : %s" % (e, datetime.now()), file=sys.stderr)
