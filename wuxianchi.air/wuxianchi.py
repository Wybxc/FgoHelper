# -*- encoding=utf8 -*-
__author__ = "忘忧北萱草"

from airtest.core.api import *
import random
using("utils.air")
from utils import ttouch, vtouch
auto_setup(__file__)

while True:
    while not ttouch(Template(r"tpl1572324718196.png", record_pos=(-0.166, 0.089), resolution=(1280, 720))):
        vtouch([0.331, 0.625])
        sleep(0.5)
#         if ttouch(Template(r"tpl1572622590486.png", record_pos=(0.389, -0.09), resolution=(1920, 1080))):
#             vtouch(Template(r"tpl1572622646487.png", record_pos=(0.155, 0.158), resolution=(1920, 1080)))
#             sleep(0.25)
#             vtouch(Template(r"tpl1572622666814.png", record_pos=(0.001, 0.158), resolution=(1920, 1080)))
    