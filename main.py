# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:29:05 2019

@author: Hossain
"""

import tkinter as tk
from PIL import Image, ImageTk


total=0
balls = 0
over = 0
b1_run = 0
b2_run = 0
b3_run = 0
b4_run = 0
b5_run = 0
b6_run = 0

team_A = ['Tower', 'Dipankar', 'Ashiqur', 'Xubaer', 'Arefin', 'Ikteaja']
team_B = ['Turnab', 'Jaser', 'Shatil', 'Shafat', 'Tonoy', 'Farhad']


def count_batsman_run(run):
    global b1_run, b2_run, b3_run, b4_run, b5_run, b6_run
    if (striker == batsman_1) :
        b1_run += run
        batsman_1.config(text=b1_run)
    elif (striker == batsman_2) :
        b2_run += run
        batsman_2.config(text=b2_run)
    elif (striker == batsman_3) :
        b3_run += run
        batsman_3.config(text=b3_run)
    elif (striker == batsman_4) :
        b4_run += run
        batsman_4.config(text=b4_run)
    elif (striker == batsman_5) :
        b5_run += run
        batsman_5.config(text=b5_run)
    else:
        b6_run += run
        batsman_6.config(text=b6_run)


def wicket():
    a=1

def is_over():
    global over, balls
    if (balls%6==0):
        balls=0
        over+=1
        return True
    else:
        return False

def change_batsman(b_1, b_2):
    global striker, non_striker
    if (not is_over()):
        striker, non_striker = b_2, b_1
    

def add_run(run,wide=0):
    global total, balls, striker, non_striker

    if (wide == 1):
        total += run
    else:
        total += run
        balls+=1
        if (run%2 == 1):
            count_batsman_run(run)
            change_batsman(striker, non_striker)
        else:
            count_batsman_run(run)
    run_total.config(text=total)
    is_over()
    tot_over = over + balls/10
    ball_total.config(text=tot_over)
    

window = tk.Tk()
window.title("Welcome to Tiger's cricket den Scorer app")
window.geometry('400x600')

logo = Image.open("umpire_1.gif")
cricket_logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(window, image=cricket_logo)
logo_label.image = cricket_logo
logo_label.place(x=200, y=0)

#logo = tk.PhotoImage(file="umpire_1.gif")               
#tk.Label(window, image=logo).grid(column=1)
tk.Label(window, text="Tiger's cricket den.").grid(row=1, columnspan=3)


tk.Button(window,text='Zero', width=25, command=lambda : add_run(0)).grid(row=2, columnspan=3)
tk.Button(window,text='One run', width=25, command=lambda : add_run(1)).grid(row=3, columnspan=3)
tk.Button(window,text='Two run', width=25, command=lambda : add_run(2)).grid(row=4, columnspan=3)
tk.Button(window,text='Three run', width=25, command=lambda : add_run(3)).grid(row=5, columnspan=3)
tk.Button(window,text='Four run', width=25, command=lambda : add_run(4)).grid(row=6, columnspan=3)
tk.Button(window,text='Six run', width=25, command=lambda : add_run(6)).grid(row=7, columnspan=3)
tk.Button(window,text='Wide', width=25, command=lambda : add_run(1,1)).grid(row=8, columnspan=3)



tk.Label(window, text=team_A[0], bg="red", fg="white").grid(row=9, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
batsman_1 = tk.Label(window, bg='white')
batsman_1.grid(row=9, column=1, sticky=tk.W+tk.E, padx=1, pady=5)
tk.Button(window,text='Out', command=lambda : wicket(team_A[0])).grid(row=9, column=2, sticky=tk.W+tk.E, padx=1, pady=5)


tk.Label(window, text=team_A[1], bg="red", fg="white").grid(row=10, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
batsman_2 = tk.Label(window, bg='white')
batsman_2.grid(row=10, column=1, sticky=tk.W+tk.E, padx=1, pady=5)
tk.Button(window,text='Out', command=lambda : wicket(team_A[1])).grid(row=10, column=2, sticky=tk.W+tk.E, padx=1, pady=5)


tk.Label(window, text=team_A[2], bg="red", fg="white").grid(row=11, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
batsman_3 = tk.Label(window, bg='white')
batsman_3.grid(row=11, column=1, sticky=tk.W+tk.E, padx=1, pady=5)
tk.Button(window,text='Out', command=lambda : wicket(team_A[2])).grid(row=11, column=2, sticky=tk.W+tk.E, padx=1, pady=5)


tk.Label(window, text=team_A[3], bg="red", fg="white").grid(row=12, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
batsman_3 = tk.Label(window, bg='white')
batsman_3.grid(row=12, column=1, sticky=tk.W+tk.E, padx=1, pady=5)
tk.Button(window,text='Out', command=lambda : wicket(team_A[3])).grid(row=12, column=2, sticky=tk.W+tk.E, padx=1, pady=5)


striker = batsman_1
non_striker = batsman_2

tk.Label(window, text="Total Run", bg="red", fg="white").grid(row=17, rowspan=2, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
run_total= tk.Label(window, bg='white')
run_total.grid(row=17, rowspan=2, column=1, columnspan=2, sticky=tk.W+tk.E)

tk.Label(window, text="Overs", bg="red", fg="white").grid(row=19, rowspan=2, column=0, padx = 10, pady = 5, sticky=tk.W+tk.E)
ball_total= tk.Label(window, bg='green')
ball_total.grid(row=19, rowspan=2, column=1, columnspan=2, sticky=tk.W+tk.E)




window.mainloop()
