# Program reads a file and prints to stdout the specified number of the longest lines
# that are sorted based on their length in descending order.
#
# Your program should accept a path to a file as its first argument. The file contains multiple lines.
# The first line indicates the number of lines you should output,
# the other lines are of different length and are presented randomly.
# You may assume that the input file is formatted correctly and the number is a valid positive integer.
#
# INPUT SAMPLE:
# 2
# Hello World
# CodeEval
# Quick Fox
# A
# San Francisco
#
# OUTPUT SAMPLE:
# San Francisco
# Hello World
#
# Print out the longest lines limited by specified number and sorted by their length in descending order.

# My original attempt
# def longest_lines(file):
#     with open(file, 'r+') as f:
#         # number_of_lines = int(f.readline())
#         print max(open(file, 'r+'), key=len)
#
# longest_lines("longest_lines.txt")



# Other ways to approach the problem
# Store the len with the key. Sort the print whatever amount of lines it asks for.


# loop over and have it sorted longest to shortest, then print out the number of lines that it asks for.
def longest_lines(file):
    with open(file, 'r+') as f:
        number_of_lines = int(f.readline())
        sorted_list = sorted(open(file, 'r+'), key=len, reverse=True)
        longest_list = []
        for word in sorted_list:
            longest_list.append(word.strip('\n'))
        print '\n'.join(longest_list[0:number_of_lines])

longest_lines("longest_lines.txt")



# Final Solution

# import sys

# f = open(sys.argv[1], 'r+')
# number_of_lines = int(f.readline())
# sorted_list = sorted(open(file, 'r+'), key=len, reverse=True)
# longest_list = []
# for word in sorted_list:
#     longest_list.append(word.strip('\n'))
# print '\n'.join(longest_list[0:number_of_lines])