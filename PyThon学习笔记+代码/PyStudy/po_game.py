#  -*- coding:utf-8 -*-
import random

map = 10

ant_point = random.randint(0,map)
worm_point = random.randint(0,map)
print('ant_point:',ant_point,'worm_point:',worm_point)

step = [-2,+2,-3,+3]

while ant_point != worm_point:
    astep = random.choice(step)
    if 0 <= ant_point + astep <= map:
        ant_point += astep
        
    astep = random.choice(step)
    if 0 <= worm_point + astep <= map:
        worm_point += astep
        
    print('ant_point:',ant_point,'worm_point:',worm_point)
