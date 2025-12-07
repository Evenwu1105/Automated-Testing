from airtest.core.settings import Settings as ST
__author__ = "Evenwu"

from airtest.core.api import *

auto_setup(__file__)


def battle_1():
    dev = connect_device("Android:///")
    i=0
    touch_customize(Template(r"./res/tpl1765099664521.png", record_pos=(0.006, 0.609), resolution=(1260, 2720)))
    touch_customize(Template(r"./res/tpl1765109392534.png", record_pos=(0.026, -0.597), resolution=(1260, 2720)))

    if exists(Template(r"./res/tpl1765111415520.png", record_pos=(0.087, -0.016), resolution=(1260, 2720))):
        sleep(0.5)
        touch_customize(Template(r"./res/tpl1765111415520.png", record_pos=(0.087, -0.016), resolution=(1260, 2720)))
    else :
        print('Not Found')
        wait("NEW")
    if exists(Template(r"./res/tpl1765111187340.png", record_pos=(0.409, -0.823), resolution=(1260, 2720))):
        touch_customize(Template(r"./res/tpl1765111187340.png", record_pos=(0.409, -0.823), resolution=(1260, 2720)))
    sleep(2.0)    
    touch_customize((336,824))
    sleep(2.0)
    touch_customize((630,660))

    touch_customize(Template(r"./res/tpl1765100565066.png", record_pos=(0.002, 0.889), resolution=(1260, 2720)))
    

        

    i=0
    while(i<10):
        try:
            swipe((200,1800),(1100,1800))
            wait(Template(r"./res/tpl1765105069888.png", record_pos=(0.231, -0.207), resolution=(1260, 2720)))
        except:
            print("2")
        i=i+1
        try:

            if(exists_customize(Template(r"./res/tpl1765102940404.png", record_pos=(0.279, -0.7), resolution=(1260, 2720)))):
                print("11111111111111111111111111111111111111111111111111")
                while not exists_customize(Template(r"./res/tpl1765109809591.png", record_pos=(-0.4, 0.894), resolution=(1260, 2720))):
                    touch_customize((0,0))
                    sleep(0.5)
                break
            elif(exists_customize(Template(r"./res/tpl1765105574314.png", record_pos=(-0.003, -0.686), resolution=(1260, 2720)))):
                while not exists_customize(Template(r"./res/tpl1765109809591.png", record_pos=(-0.4, 0.894), resolution=(1260, 2720))):
                    touch_customize((0,0))
                    sleep(0.5)
              
                break
        except:
            print("1")


    fontpage=wait(Template(r"./res/tpl1765109809591.png", record_pos=(-0.4, 0.894), resolution=(1260, 2720)),timeout=3)
    touch_customize(fontpage)

    assert_exists(Template(r"./res/tpl1765106507921.png", record_pos=(-0.398, 0.895), resolution=(1260, 2720)),"Not Found")

for i in range(5):
    battle_1()