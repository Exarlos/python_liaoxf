'''
Author: your name
Date: 2022-03-14 15:39:30
LastEditTime: 2022-03-15 17:00:06
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Coding\BaiduNetdiskWorkspace\Python\01awesome-python3-webapp\test_sql.py
'''
# from orm import orm
import time
import json
import os
from aiohttp import web
from datetime import datetime
import orm
import asyncio
from models import User, Blog, Comment

import logging

logging.basicConfig(level=logging.INFO)

# routes = web.RouteTableDef()


# @routes.get('/')
# async def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def my_app():
    app = web.Application()
    # app.add_routes(routes)
    return app


async def test(loop):                      # *** 注意此处的密码填自己设的密码 ***
    await orm.create_pool(loop=loop, user='root', password='369874125', db='moe')
    # *** 注意此处的密码填自己设的密码 ***
    u = User(name='Test', email='test@qq.com',
             passwd='1234567890', image='about:blank')
    await u.save()
    # 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()

web.run_app(my_app(), host='127.0.0.1', port=9000)
