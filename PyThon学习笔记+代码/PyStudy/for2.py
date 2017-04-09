#  -*- coding:utf-8 -*-

# if statement example

number=59
num_chances=3
print("你只有3次机会！！！")


for i in range(1,num_chances+1):
    print("这是第",i,"次机会！")
    guess = int(input("Enter an interger: "))

    if guess==number:
        print("Bingo !   you guessed it right.")
        print('(but you do not win any prizes!)')
        break
    elif guess < number:
        print('oh no,你猜的太低了,还有',str(num_chances - i),"次机会！")
    else:
        print('oh no,你猜的太高了',str(num_chances - i),"次机会！")
    
    
print('done')


