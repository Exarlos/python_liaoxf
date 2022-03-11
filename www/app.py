'''
Author: your name
Date: 2022-03-09 17:03:22
LastEditTime: 2022-03-10 18:05:32
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Coding\BaiduNetdiskWorkspace\Python\01awesome-python3-webapp\www\app.py
'''

# import asyncio
# from aiohttp import web
# from datetime import datetime
# import time
# import json
# import os
# import logging
# logging.basicConfig(level=logging.INFO)


# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


# async def init(loop):
#     app = web.Application()
#     # app.router.add_route('GET', '/', index)
#     app.add_routes([web.get("/", index)])
#     apprunner = web.AppRunner(app)
#     await apprunner.setup()

#     srv = await loop.create_server(apprunner.server, '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv


# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

import logging;

logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def my_app():
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(my_app(), host='127.0.0.1', port=9000)