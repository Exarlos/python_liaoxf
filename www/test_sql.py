'''
Author: your name
Date: 2022-03-14 15:39:30
LastEditTime: 2022-03-16 15:47:46
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
import functools

import logging

logging.basicConfig(level=logging.INFO)


async def my_app():
    app = web.Application()
    # app.add_routes(routes)
    return app

loop = asyncio.get_event_loop()


async def test():                      # *** 注意此处的密码填自己设的密码 ***
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    # *** 注意此处的密码填自己设的密码 ***
    # u = User(name='Test', email='test223422@qq.com',
    #  passwd='1234567890', image='about:blank')

    usa = await User.find('001647410890640695cd43d2a7d45e3931c5ed434426e30000')
    print(usa)
    await usa.remove()
    # await u.save()
    # 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()


def test2(func):  # 定义装饰器
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # 将创建连接池的方法放在func前面执行
        await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
        return await func(*args, **kwargs)
    return wrapper


@test2  # 将orm.create_pool方法抽取出来，通过装饰器的形式调用
async def testUserSave(loop):
    u = User(name='Test', email='test@example.com',
             passwd=1234567890, image='about:blank')
    await u.save()


@test2
async def testUserUpdate(loop):
    pass


@test2
async def testUserSelect(loop):
    pass


@test2
async def testUserdelete(loop):
    pass


def main():

    loop.run_until_complete(test())
    print("开始发送邮件：")


if __name__ == '__main__':
    main()
