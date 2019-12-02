# -*- encoding=utf8 -*-
__author__ = "忘忧北萱草"

from airtest.core.api import *
import random

auto_setup(__file__)

width, height = device().get_current_resolution()
offset_x, offset_y = 0, 0
print('resolution: {width}x{height}'.format(width=width, height=height))
if width/height > 16/9:
    offset_x = (width - height * 16/9) * 0.5
    width = height * 16/9
if width/height < 16/9:
    offset_y = (height - width * 9/16) * 0.5
    height = width * 9/16

    
def vtouch(v, delta=30):
    if isinstance(v, Template):
        v = wait(v)
        x, y = v
    else:
        x, y = v
        if x < 1 or y < 1:
            x *= width + offset_x
            y *= height + offset_y
    x = x + (0.5 - random.random()) * delta
    y = y + (0.5 - random.random()) * delta
    return touch((x, y))


def ttouch(v, delta=30):
    f = find_all(v)
    if f:
        vtouch(f[0]['result'], delta=delta)
    return f


def mwait(v_list, interval=0.5, timeout=20, intervalfunc=None):
    for i in range(int(timeout/interval)):
        for i, v in enumerate(v_list):
            f = find_all(v)
            if f:
                return i, f[0]['result']
        else:
            if intervalfunc:
                intervalfunc()
            sleep(interval)
    else:
        return -1
    
def exists_ac(v, interval=0.3, timeout=-1):
    if timeout < 0:
        timeout = ST.FIND_TIMEOUT_TMP
    for i in range(int(timeout/interval)):
        f = find_all(v)
        if f:
            return f[0]['result']
    else:
        return False
    