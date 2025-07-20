#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: Sunday, July 6, 2025
@Author: Group 3
@Course: INF 6050
@University: Wayne State University
@Assignment: Group Assignment

@Python Version: 3.12
@Required Modules: time

@Description: This program creates a module to provide the program directions.
"""

import time

print("\n"*3)
print("-"*30)
print("Hello! I'm your Wordle Helper program. ", end="")
time.sleep(2)
print("Tell me a word and I'll tell you if its a good Wordle guess.")
time.sleep(2)
print("\nA good guess is a word that:")
time.sleep(2)
print("• Is 5 letters long")
time.sleep(2)
print("• Has not been a Wordle word before")
time.sleep(2)
print("• Is in the game's original code")
time.sleep(2)
print("\nGuess as many words as you want, and type 'QUIT' at any time to \
exit the application.")
time.sleep(2)
print("\nOkay, let's get Wordling!")
print("-"*30)
