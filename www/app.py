import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os ,json ,time
from datetime import datetime
from aiohttp import web
import sys

def index(request):
      return web.Response(body=u'<h1>Awesome</h1>', content_type='text/html',charset='utf-8')

@asyncio.coroutine
def init( loop):
    ip = sys.argv[1]
    port = sys.argv[2]
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    srv =yield from loop.create_server(app.make_handler(), ip ,port)
    print('server started at http://%s:%s...' % (ip,port))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()