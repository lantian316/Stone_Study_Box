#  -*- coding:utf-8 -*-

from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

# root = Tk()
# w = Label(root,text = "Label Title")
# w.pack()
# 
# mb.showinfo("welcom", "welcom,message")
# guess = dl.askinteger("number", "Enter a number")
# output = "this is output message"
# mb.showinfo("output:", output)

#-------------------------------------
root = Tk()
w = Label(root,text = "猜数字游戏")
w.pack()

mb.showinfo("welcom", "欢迎来到猜数字游戏")

number=59
guess_flage=False

while 1:
    guess = dl.askinteger("number", "what is your guess")
    if guess==number:
        guess_flage=True
        output="Bingo !   you guessed it right."
        mb.showinfo("hint:", output)
        break
    elif guess < number:
        output="oh no,你猜的太di了,请继续！！！"
        mb.showinfo("hint:", output)
    else:
        output="oh no,你猜的太高了,请继续！！！"
        mb.showinfo("hint:", output)
        print('')
    
    
mb.showinfo("hint:", "game over")