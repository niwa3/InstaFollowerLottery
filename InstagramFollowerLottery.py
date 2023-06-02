#!/usr/bin/env python
# -*- coding: utf8 -*-
# This program is made by @niwa3.

import instaloader
import random
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("InstagramFollowerLottery")
root.geometry("400x550")
root.resizable(0, 0)

Headline = tkinter.Label(root, text="InstagramFollowerLottery", font=("Arial", 20))
Headline.pack()

UserIdLabel = tkinter.Label(root, text="Enter your Instagram ID (Don't use important account.):", font=("Arial", 14))
UserIdLabel.pack()
UserId = tkinter.Entry(root, width=30)
UserId.pack()

UserPassLabel = tkinter.Label(
    root, text="Enter your Instagram Password:", font=("Arial", 14)
)
UserPassLabel.pack()
UserPass = tkinter.Entry(root, width=30)
UserPass.pack()

TargetLabel = tkinter.Label(root, text="Enter target Instagram ID:", font=("Arial", 14))
TargetLabel.pack()
Target = tkinter.Entry(root, width=30)
Target.pack()

NumberLabel = tkinter.Label(
    root, text="Enter the number of followers you want to get:", font=("Arial", 14)
)
NumberLabel.pack()
Number = tkinter.Entry(root, width=10)
Number.pack()

def StartButton():
    try:
        userid = UserId.get()
        password = UserPass.get()
        number = int(Number.get())
        target = Target.get()

        loader = instaloader.Instaloader()
        loader.login(userid, password)

        profile = instaloader.Profile.from_username(loader.context, target)

        followers = profile.get_followers()

        l = []
        for follower in followers:
            l.append(follower.username)

        r = []
        for i in range(number):
            rand = random.randint(0, len(l) - 1)
            r.append(l[rand])
            del l[rand]

        messagebox.showinfo("Result", "\n".join(r))
    except Exception as e:
        messagebox.showerror("Error", e)


StartButton = tkinter.Button(
    text="Submit", width=5, command=StartButton, font=("Arial", 14)
)
StartButton.pack()

root.mainloop()
