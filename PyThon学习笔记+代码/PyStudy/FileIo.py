#  -*- coding:utf-8 -*-

some_string = '''\
i love learning python
because python is fun
and also easy to use
'''

# f = open('some_str.txt', 'w')
# f.write(some_string)
# f.close()

f = open('some_str.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0 :
        break
    print(line)
f.close()