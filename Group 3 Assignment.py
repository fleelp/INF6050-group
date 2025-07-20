#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: Sunday, July 6, 2025
@Author: Group 3
@Course: INF 6050
@University: Wayne State University
@Assignment: Group Assignment

@Python Version: 3.12
@Required Modules: csv, wordledirections, sys

@Description: This program tells the user if a word is a good wordle guess.
"""

import csv #  Module to work with csv files.
import wordledirections #  Module for written directions.
import sys#  Module to quit the program.


# Load words from CSV files
def load_csv(filename):
    with open(filename, newline='') as f:
        return set(row[0].strip().lower() for row in csv.reader(f) if row)


# Define a function to quit the program.
def quit():
    print("\U0001F44B  Happy Wordling! See you next time.")
    sys.exit()


# Confirm that source files are accessible.
try:
    open("past-answers.csv")
except FileNotFoundError:
    print("The program encountered an error with source files. Please check \
your files and try again.")
    sys.exit()
try:
    open("possible-wordles.csv")
except FileNotFoundError:
    print("The program encountered an error with source files. Please check \
your files and try again.")
    sys.exit()
# Load the word lists
past_answers = load_csv("past-answers.csv")
valid_words = load_csv("possible-wordles.csv")

# Assign input from user.
word = input("What's your word?\n>>> ").strip().lower()

# While loop to allow for quitting at any time.
while word != "quit":
    # Check for valid guess
    if word not in past_answers and word in valid_words:
        print(f"✅'{word}' has not been a Wordle answer and is a good guess.")
        word = input("\nWhat's your next word?:\n>>>").strip().lower()
# Check if input contains any non-letters.
    elif word.isalpha() is False:
        print("❌ Wordle words can only contain letters. Try again.")
        word = input("\nWhat's your next word?:\n>>>").strip().lower()
# Check if input is 5 characters long.
    elif len(word) != 5:
        print(f"❌ '{word}' is not 5 letters. Try again.")
        word = input("\nWhat's your next word?:\n>>>").strip().lower()
# Check for a word that has been guessed before.
    elif word in past_answers:
        print(f"❌ '{word}' has already been a Wordle answer. Try again.")
        word = input("\nWhat's your next word?:\n>>>").strip().lower()
# Check for a word that is not in the word bank.
    elif word not in valid_words:
        print(f"❓ '{word}' is not in the original Wordle bank, so it's \
likely not a good guess. Try again.")
        word = input("\nWhat's your next word?:\n>>>").strip().lower()
# Quit if user input is quit.
else:
    quit()
