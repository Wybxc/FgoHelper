# -*- encoding=utf8 -*-
__author__ = "忘忧北萱草"

from airtest.core.api import *
import random
using("utils.air")
from utils import *
auto_setup(__file__)

points = 100000
count = int(points/2000)



for i in range(count):
    vtouch(Template(r"tpl1572273606796.png", record_pos=(0.145, 0.152), resolution=(1280, 720)))
    sleep(1.5)
    vtouch([0.657, 0.785])
    while not ttouch(Template(r"tpl1572273685570.png", record_pos=(0.096, 0.245), resolution=(1280, 720))):
        vtouch([0.963, 0.751])
        sleep(0.5)
    