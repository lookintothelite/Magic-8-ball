#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:44:19 2019
@author: john
My Python version of a magic 8 ball.
"""
import random
import os
import time

ballanswers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes','Most likely','Outlook good','YES','Signs point to yes','Reply hazy, try again','Ask again later', 'Better not tell you now','Cannot predict now','Concentrate and ask again','My reply is no','Don\'t count on it','My sources say no','Outlook not so good','Very doubtful']

random.shuffle(ballanswers)

play = input("\nWould you like to ask the magic 8 ball a yes/no question? y or n: ")

if play == 'y':
    os.system('clear')
    time.sleep(1)
    print("Concentrate on your question.\n")
    time.sleep(3)
    print("You aren't concentrating hard enough!" )
    time.sleep(3)
    while play == 'y':
        os.system('clear')
        time.sleep(4)
        print(random.choice(ballanswers))
        time.sleep(3)
        play = input("Try again? y or n: ")
    else:
        print("\n\nThank you for playing with my magic 8 ball!")
else:
    print("\n\nI didn't want to answer anyway, so bugger off!")