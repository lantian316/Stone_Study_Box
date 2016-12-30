# -*- coding: utf-8 -*-


def by_name(t) :
    return t[0].lower()

def by_core(t) :
    return int(t[1])


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_core,reverse=True)
print(L2)

人生苦短 = "人生苦短，我用python"
print(人生苦短)



g=lambda x,y:x*y

print(g(4,6))


import functools
def log(text1,text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text1, func.__name__))
            res = func(*args, **kw)
            print('%s %s():' % (text2, func.__name__))
            return res
        return wrapper
    return decorator

@log('begin call','end call')
def now():
    print('2015-3-25')

now()

print('我那个去，日了个狗了。。。。。。。。。。。。')
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


















