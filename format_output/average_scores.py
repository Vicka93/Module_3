"""
Author:Viktoriia Denys
Program:average_scores.py
program average_scores.py  reads in one person's names, first and last, their age and three scores out of 100.
Taking the three scores and finding the average, storing into a variable.
"""


AMT_OF_SCORES = 3


def average():
    score1 = input("Enter your your first grade:")
    score2 = input("Enter your your second grade:")
    score3 = input("Enter your your third grade:")
    return (int(score1) + int(score2) + int(score3)) / AMT_OF_SCORES


if __name__ == '__main__':
    lastName = input("Enter your last name:")
    firstName = input("Enter your first name:")
    age = input("Enter your age:")
