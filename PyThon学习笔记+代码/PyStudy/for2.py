#  -*- coding:utf-8 -*-

# if statement example

number=59
num_chances=3
print("��ֻ��3�λ��ᣡ����")


for i in range(1,num_chances+1):
    print("���ǵ�",i,"�λ��ᣡ")
    guess = int(input("Enter an interger: "))

    if guess==number:
        print("Bingo !   you guessed it right.")
        print('(but you do not win any prizes!)')
        break
    elif guess < number:
        print('oh no,��µ�̫����,����',str(num_chances - i),"�λ��ᣡ")
    else:
        print('oh no,��µ�̫����',str(num_chances - i),"�λ��ᣡ")
    
    
print('done')


