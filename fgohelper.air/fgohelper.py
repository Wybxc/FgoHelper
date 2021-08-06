# -*- encoding=utf8 -*-
__author__ = "忘忧北萱草"

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.WARNING)

from airtest.core.api import *
ST.FIND_TIMEOUT_TMP = 1.5
using("utils.air")
from utils import *
import random
auto_setup(__file__)

repeat_count = 28
use_gold_apple = True
use_order_change = False
guest = Template(r"tpl1573214186909.png", record_pos=(-0.396, -0.072), resolution=(1280, 720))
# guest = [Template(r"tpl1628209519321.png", threshold=0.5999999999999999, record_pos=(-0.374, -0.04), resolution=(1600, 900)), Template(r"tpl1628209546240.png", threshold=0.5999999999999999, record_pos=(-0.374, 0.115), resolution=(1600, 900))]

# guest = Template(r"tpl1574696001602.png", record_pos=(-0.398, 0.084), resolution=(1280, 720))
# guest = Template(r"tpl1598748597104.png", record_pos=(-0.398, 0.098), resolution=(1280, 720))

# 绿卡队（3T）
settings = [
    [{'skill':[6], 'noble':[2], 'card':'BAQ'}, {}],
    [{'skill':[3, 4, 7, 8, 6], 'noble':[1], 'card':'BAQ', 'aim':1}, {}],
    [{'skill':[1, 2, -2, -3, 5, 9], 'noble':[1, 2, 3], 'card':'BQA', 'aim':2},{'aim':2, 'noble':[1, 2, 3], 'card':'BQA'}],
]

# 换人礼装测试
# settings = [
#     [{'skill': [[-3, (2, 4)]]}, {}], [{}, {}], [{}, {}]
# ]

# 陈宫（3T）
# settings = [
#     [{'skill': [2, 5, 6, 8, 9], 'noble': [1], 'card': 'AQB'}, {}],
#     [{'skill': [5, 6], 'noble': [1], 'card': 'AQB'}, {}],
#     [{'skill': [4, 6, -2], 'noble': [1], 'card': 'AQB', 'aim': 1}, {'noble': [1], 'card': 'AQB'}]
# ]

# 绿卡队（2T）
# settings = [
#     [{'skill':[6], 'noble':[2], 'card':'BAQ'},{}],
#     [{'skill':[3, 4, 7, 8, 6], 'noble':[1], 'card':'BAQ', 'aim':1},{'skill':[1, 2, -2, -3, 5, 9], 'noble':[1, 2, 3], 'card':'BQA', 'aim':2},{'aim':2, 'noble':[1, 2, 3], 'card':'BQA'},{}],
#     [{}],
# ]

# settings = [
#     [{'skill':[1, 7], 'noble':[], 'card':'ABQ', 'weak':False},{'card':'ABQ', 'weak':False}],
#     [{'skill':[4, 5], 'noble':[2], 'card':'ABQ', 'aim':1, 'weak':False},{'card':'ABQ', 'noble':[2], 'weak':False}],
#     [{'skill':[2, 3, -2, -3, 5, 6, 8, 9], 'noble':[1, 2, 3], 'card':'ABQ', 'aim':2}, {'aim':2, 'card':'ABQ', 'noble':[1, 2, 3]}],
# ]

# 平A
# settings = [
#     [{}], [{}], [{'skill':[6, 9], 'noble': [2, 1]}]
# ]

# settings = [
#     [{'skill':[1,2,4,5,6,7,9,-1,-2], 'noble':[3,2,1], 'card':'BQA'}, {'skill':[3],'noble':[3,2,1], 'card':'BQA'},{'skill':[],'noble':[3,2,1], 'card':'BQA'},{'skill':[],'noble':[3,2,1], 'card':'BQA'},{'skill':[],'noble':[3,2,1], 'card':'BQA'},{'skill':[8],'noble':[3,2,1], 'card':'BQA'}]
# ]

USE_ENGLISH = False
battle_menu = Template(r"tpl1572102737403.png", record_pos=(0.43, -0.118), resolution=(1920, 1080))
battle_finish = Template(r"tpl1572134713930.png", record_pos=(-0.003, -0.234), resolution=(1920, 1080))

if USE_ENGLISH:
    arts = Template(r"tpl1571981302645.png", rgb=True, record_pos=(0.205, 0.16), resolution=(1280, 720))
    buster = Template(r"tpl1571842613709.png", threshold=0.6, rgb=True, record_pos=(0.209, 0.163), resolution=(1280, 720))
    quick = Template(r"tpl1571981133472.png", threshold=0.6, rgb=True, record_pos=(-0.19, 0.172), resolution=(1280, 720))
else:    
    arts = [Template(r"tpl1628205010051.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.19, 0.169), resolution=(1600, 900)),Template(r"tpl1628205328213.png", threshold=0.5999999999999999, record_pos=(-0.218, 0.166), resolution=(1600, 900))]
    buster = [Template(r"tpl1628204791883.png", threshold=0.5999999999999999, rgb=True, record_pos=(0.203, 0.161), resolution=(1600, 900)),Template(r"tpl1628205354400.png", threshold=0.5999999999999999, record_pos=(0.181, 0.164), resolution=(1600, 900))]
    quick = [Template(r"tpl1628204875542.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.396, 0.163), resolution=(1600, 900)),Template(r"tpl1628205372065.png", threshold=0.5999999999999999, record_pos=(-0.018, 0.166), resolution=(1600, 900))]
weak = [Template(r"tpl1628205045859.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.142, 0.022), resolution=(1600, 900)), Template(r"tpl1628205400122.png", threshold=0.8, rgb=False, record_pos=(-0.351, 0.011), resolution=(1600, 900))]
resist = [Template(r"tpl1628206818620.png", threshold=0.5999999999999999, rgb=True, record_pos=(-0.339, 0.015), resolution=(1600, 900)), Template(r"tpl1628206868485.png", threshold=0.8, record_pos=(-0.351, 0.005), resolution=(1600, 900))]
attack = Template(r"tpl1575520639093.png", threshold=0.8, target_pos=4, record_pos=(0.451, 0.192), resolution=(1280, 720))
battles = [[Template(r"tpl1572044714997.png", threshold=0.85, record_pos=(0.194, -0.261), resolution=(1920, 1080)),Template(r"tpl1574610591486.png", threshold=0.8500000000000001, record_pos=(0.196, -0.26), resolution=(1280, 720)),Template(r"tpl1573214400260.png", threshold=0.85, record_pos=(0.195, -0.261), resolution=(1280, 720)),Template(r"tpl1581556537739.png", threshold=0.85, record_pos=(0.194, -0.263), resolution=(1280, 720)),Template(r"tpl1573209950447.png", threshold=0.85, record_pos=(0.195, -0.262), resolution=(1280, 720))],[Template(r"tpl1572044768044.png", threshold=0.87, record_pos=(0.193, -0.263), resolution=(1920, 1080)),Template(r"tpl1573534028433.png", threshold=0.87, record_pos=(0.195, -0.263), resolution=(1280, 720)),Template(r"tpl1573214509933.png", threshold=0.8500000000000002, record_pos=(0.195, -0.261), resolution=(1280, 720)),Template(r"tpl1581557622159.png", record_pos=(0.193, -0.262), resolution=(1280, 720))],[Template(r"tpl1572017870330.png", threshold=0.85, record_pos=(0.195, -0.262), resolution=(1280, 720))]]
aims = [[0.083, 0.329], [0.233, 0.316], [0.404, 0.341]]
cards = list(zip([0.094, 0.290, 0.492, 0.695, 0.900], [0.694]*5))
skills = list(zip([0.046, 0.121, 0.195, 0.296, 0.371, 0.445, 0.546, 0.621, 0.695], [0.791]*9))
nobles = [(0.328, 0.300), (0.492, 0.300), (0.656, 0.300)]


def check_in_battle():
    if find_all_plus(Template(r"tpl1571999067389.png", record_pos=(-0.001, -0.202), resolution=(1920, 1080))) or find_all_plus(Template(r"tpl1571999091335.png", record_pos=(0.004, -0.205), resolution=(1920, 1080))) or find_all_plus(Template(r"tpl1571999511599.png", record_pos=(0.002, -0.159), resolution=(1920, 1080))):
        vtouch(Template(r"tpl1571999190864.png", record_pos=(0.328, -0.211), resolution=(1920, 1080)))


def use_skill(index, target=1, master=False):
    confirm = None
    while not confirm:
        if not master:
            vtouch(skills[index - 1])
            check_in_battle()
        else:
            vtouch(Template(r"tpl1571981836706.png", record_pos=(0.43, -0.037), resolution=(1280, 720)))
            vtouch((0.633 + index * 0.070, 0.417))            
            check_in_battle()
        sleep(0.5)
        confirm = find_all_plus(Template(r"tpl1571892861311.png", threshold=0.7, record_pos=(0.163, 0.049), resolution=(1280, 720)))    
    confirm = confirm[0]['result']        
    if confirm[0]/width > 0.5:
        vtouch(confirm)
        sleep(0.8)
        if use_order_change and master and index == 3:
            # 换人礼装
            a, b = target
            vtouch((0.1 + (a-1) * 0.156, 0.5))
            sleep(0.2)
            vtouch((0.1 + (b-1) * 0.156, 0.5))
            sleep(0.2)
            ttouch(Template(r"tpl1628207848453.png", record_pos=(0.004, 0.208), resolution=(1600, 900)))
        if find_all_plus(Template(r"tpl1571981495644.png", record_pos=(0.002, -0.13), resolution=(1280, 720))):
            sleep(0.1)
            vtouch((0.25 + (target-1) * 0.246, 0.625))
            sleep(0.3)
    else:
        ttouch(Template(r"tpl1571892908291.png", record_pos=(-0.168, 0.051), resolution=(1280, 720)))
        sleep(0.3)
    check_in_battle()        
    wait(battle_menu)
           

def analyze_cards():
    wait(Template(r"tpl1589849523786.png", record_pos=(0.436, 0.251), resolution=(1280, 720)))
    sleep(0.3)
    result = []
    for i in range(5):
        result.append({'type':'Arts', 'weak':0})
    def get_position(v):
        f = find_all_plus(v)
        return [s['result'][0] / width for s in f if s['result'][1] > 0.45*height] if f else []

    for x in get_position(buster):
        result[int(x/0.2)]['type'] = 'Buster'
    for x in get_position(arts):
        result[int(x/0.2)]['type'] = 'Arts'
    for x in get_position(quick):
        result[int(x/0.2)]['type'] = 'Quick'
    for x in get_position(weak):
        result[int((x-0.059)/0.2)]['weak'] = 1
    for x in get_position(resist):
        result[int((x-0.059)/0.2)]['weak'] = -1
    print('cards: ' + ''.join([c['type'][0] for c in result]))
    print('weak: ' + str([c['weak'] for c in result]))
    return result


def get_battle():
    wait(attack)
    for i, bs in enumerate(battles):
        if find_all_plus(bs):
            return i+1
    return 0        

        
def play_round(aim=0, skill=[], noble=[], card='BAQ', weak=True):
    if aim > 0:
        vtouch(aims[aim-1])
    for s in skill:
        if isinstance(s, list) or isinstance(s, tuple):
            s, target = s
        else:
            target = 1
        if s > 0:
            use_skill(s, target=target)
        else:
            use_skill(-s, target=target, master=True)
    vtouch(attack)
    sleep(1)
    card_info = analyze_cards()
    for n in noble:
        vtouch(nobles[n-1])
    card_name = {'B':'Buster', 'A':'Arts', 'Q':'Quick'}
    card_pri = {card_name[c]:3-i for i, c in enumerate(card)}
    card_score = []
    if weak:
        for i, c in enumerate(card_info):
            card_score.append((c['weak']*5 + card_pri[c['type']], i))
    else:
        for i, c in enumerate(card_info):
            card_score.append((card_pri[c['type']], i))
    card_score.sort(key=lambda t: t[0], reverse=True)
    print('scores:' + str(card_score))
    card_cnt = 0
    for c in card_score:
        vtouch(cards[c[1]])
        card_cnt += 1
        if card_cnt >= 3:
            break            
            
            
def select_guest():
    try_cnt = 0
    while not ttouch(guest):
        if not find_all_plus(Template(r"tpl1572080305639.png", record_pos=(0.397, -0.255), resolution=(1920, 1080))):
            return
        try_cnt += 1
        swipe((0.508*width, 0.806*height), vector=[(random.random() - 0.5) * 0.01, -0.3 + random.random() * 0.01])
        if find_all_plus(Template(r"tpl1571843575054.png", record_pos=(0.47, 0.065), resolution=(1280, 720))) or try_cnt >= 10:
            try_cnt = 0
            while True:
                if ttouch(Template(r"tpl1573214218300.png", record_pos=(0.164, -0.178), resolution=(1280, 720))):
                    sleep(0.5)
                    vtouch(Template(r"tpl1571843623473.png", record_pos=(0.155, 0.156), resolution=(1280, 720)))
                    sleep(3)
                
    sleep(1)
            
        
def before_level():
    # 进入关卡
    if exists_ac(Template(r"tpl1573220121940.png", record_pos=(-0.414, -0.247), resolution=(1280, 720))):
        vtouch((0.695, 0.319))
        sleep(1)
    # 磕苹果
    if exists_ac(Template(r"tpl1572136014819.png", record_pos=(0.0, -0.226), resolution=(1920, 1080))):
        if use_gold_apple:
            vtouch(Template(r"tpl1572136064061.png", rgb=True, record_pos=(-0.202, -0.026), resolution=(1920, 1080)))
            sleep(1)
            vtouch(Template(r"tpl1572136115852.png", record_pos=(0.155, 0.157), resolution=(1920, 1080)))
            sleep(2)
        else:
            return
    # 选择助战
    sleep(2)
    if exists_ac(Template(r"tpl1572080305639.png", record_pos=(0.397, -0.255), resolution=(1920, 1080))):
        select_guest()
            
def play_level():    
    if exists_ac(Template(r"tpl1572080345669.png", record_pos=(0.401, -0.253), resolution=(1920, 1080))):
        sleep(1)
        vtouch(Template(r"tpl1571844621057.png", record_pos=(0.427, 0.242), resolution=(1280, 720)))        
    wait(attack, interval=2, timeout=240)
    for i in range(1, 4):
        round_cnt = 0
        finished = False
        while not finished and get_battle() == i:
            setting = settings[i-1]           
            if round_cnt < len(setting) - 1:
                play_round(**setting[round_cnt])
            else:
                play_round(**setting[-1])
            round_cnt += 1
            if mwait([battle_menu, battle_finish], interval=0.7, timeout=120, intervalfunc=lambda:vtouch([0.666, 0.074]))[0] == 1:
                finished = True
        if finished:
            break
    wait(battle_finish, timeout=120)
    while not ttouch(Template(r"tpl1572134881355.png", record_pos=(0.361, 0.246), resolution=(1920, 1080))):
        vtouch([0.471, 0.876])
        sleep(1.5)
    

if True:
    before_level()
    for i in range(repeat_count):
        print('Battle: ' + str(i+1))
        try:            
            play_level()
            if i != repeat_count - 1:
                sleep(1)
                vtouch(Template(r"tpl1598268548877.png", record_pos=(0.156, 0.159), resolution=(1280, 720)))
                sleep(2)
                select_guest()
        except TargetNotFoundError:
            before_level()

else:
    print(analyze_cards())
    pass

