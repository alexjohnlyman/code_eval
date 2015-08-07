#Lowercase
#
# Given a string write a program to convert it into lowercase.
# The first argument will be a path to a filename containing sentences, one per line.
# You can assume all characters are from the english language.

# INPUT SAMPLE:
# HELLO CODEEVAL
# This is some text

# OUTPUT SAMPLE:
# hello codeeval
# this is some text

# Print to stdout, the lowercase version of the sentence, each on a new line.

# Testing

# def stdout(filename):
#     input = open(filename, 'r+')
#     for line in input:
#         return line.lower()
#
# print stdout()

# def stdout(filename):
#     input = open(filename, 'r+')
#
# print stdout('lowercase.txt')

# Final answer
# import sys
#
#
# input = open(sys.argv[1], 'r+')
# for line in input:
#     print line.lower()
