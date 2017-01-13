#  -*- coding:utf-8 -*-

# if statement example

number=59
guess = int(input("Enter an interger: "))

if guess==number:
    print("Bingo !   you guessed it right.")
    print('(but you do not win any prizes!)')
elif guess < number:
    print('oh no,你猜的太低了')
else:
    print('oh no,你猜的太高了')
    
    
print('done')


