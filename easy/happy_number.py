# A happy number is defined by the following process. Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1,
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy, while those that do not end in 1 are unhappy.
#
# For the curious, here's why 7 is a happy number: 7->49->97->130->10->1.
# Here's why 22 is NOT a happy number: 22->8->64->52->29->85->89->145->42->20->4->16->37->58->89 ...
#
# INPUT SAMPLE:
# 1
# 7
# 22
# The first argument is the pathname to a file which contains test data, one test case per line.
# Each line contains a positive integer.
#
# OUTPUT SAMPLE:
# 1
# 1
# 0
# If the number is a happy number, print out 1. If not, print out 0.

# Testing
# test = 7
# def happy_or_not(number):
#     number = str(number)
#     if number == "1":
#         print 1
#     else:
#         new_num = 0
#         for i in number:
#             i = int(i)
#             new_num += i**2
#         if new_num == 10 or new_num == 10:
#             print 1
#         else:
#             try:
#                 happy_or_not(new_num)
#             except RuntimeError:
#                 print 0
# happy_or_not(test)
# def happy_number_check(file):
#     with open(file, 'r+') as f:
#         for line in f:
#             if line.strip().isdigit():
#                 happy_or_not(line.strip())
# happy_number_check("happy_numbers.txt")


# Final solution

# import sys
#
# def happy_or_not(number):
#     number = str(number)
#     if number == "1":
#         print 1
#     else:
#         new_num = 0
#         for i in number:
#             i = int(i)
#             new_num += i**2
#         if new_num == 10 or new_num == 10:
#             print 1
#         else:
#             try:
#                 happy_or_not(new_num)
#             except RuntimeError:
#                 print 0
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     if line.strip().isdigit():
#         happy_or_not(line.strip())
