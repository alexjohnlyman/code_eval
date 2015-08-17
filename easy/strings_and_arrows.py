# STRINGS AND ARROWS
# You have a string composed of the following symbols: '>', '<', and '-'.
# Your task is to find, count, and print to the output a number of arrows in the string.
# An arrow is a set of the following symbols: '>>-->' or '<--<<'.
# Note that one character may belong to two arrows at the same time (line #1).
# Each line includes a test case with a string of different length from 10 to 250 characters.
# The string consists of '>', '<', and '-' symbols.

# INPUT SAMPLE:
# <--<<--<<
# <<>>--><--<<--<<>>>--><
# <-->>

# OUTPUT SAMPLE:
# 2
# 4
# 0

# CONSTRAINTS:
# An arrow is a set of the following symbols: '>>-->' or '<--<<'.
# One symbol may belong to two arrows at the same time.
# The number of test cases is 40.

# Testing
# def strings_arrows_2(file):
#     with open(file, 'r+') as f:
#         substring = '>>-->'
#         substring_2 = '<--<<'
#         for line in f:
#             count = 0
#             for i in range(len(line)):
#                 if line[i:].startswith(substring):
#                     count += 1
#             for i in range(len(line)):
#                 if line[i:].startswith(substring_2):
#                     count += 1
#             print count
#
# strings_arrows_2("strings_and_arrows.txt")


# Final Solution

# import sys
#
# f = open(sys.argv[1], 'r+')
# substring = '>>-->'
# substring_2 = '<--<<'
# for line in f:
#     count = 0
#     for i in range(len(line)):
#         if line[i:].startswith(substring):
#             count += 1
#     for i in range(len(line)):
#         if line[i:].startswith(substring_2):
#             count += 1
#     print count
