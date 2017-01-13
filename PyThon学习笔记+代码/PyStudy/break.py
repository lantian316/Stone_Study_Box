#  -*- coding:utf-8 -*-

number=59


while True:
    guess = int(input("Enter an interger: "))
    if guess==number:
        print("Bingo !   you guessed it right.")
        print('(but you do not win any prizes!)')
        break
    elif guess < number:
        print('oh no,你猜的太低了,请继续！！！')
        continue
    else:
        print('oh no,你猜的太高了,请继续！！！')
    
print('done')

