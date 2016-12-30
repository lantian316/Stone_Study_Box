#  -*- coding:utf-8 -*-

number=59
guess_flage=False

while guess_flage == False:
    guess = int(input("Enter an interger: "))
    if guess==number:
        guess_flage=True
        print("Bingo !   you guessed it right.")
        print('(but you do not win any prizes!)')
    elif guess < number:
        print('oh no,你猜的太低了,请继续！！！')
    else:
        print('oh no,你猜的太高了,请继续！！！')
    
    
print('done')

