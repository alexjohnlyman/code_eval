# SUM OF DIGITS
# Given a positive integer, find the sum of its constituent digits.

# INPUT SAMPLE:
# The first argument will be a path to a filename containing positive integers, one per line. E.g.

# 23
# 496

# OUTPUT SAMPLE:
# Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

# 5
# 19

# x = 12345
# total = 0
# y = str(x)
# for i in y:
#     z = int(i)
#     total += z
#
# print total

# For Testing
# def sum_digits(filename):
#     f = open(filename, 'r+')
#     for line in f:
#         if line == "":
#             continue
#         else:
#             full_line = ""
#             for num in line:
#                 full_line += str(num)
#         full_line = int(full_line)
#         print sum(map(int, str(full_line)))

# sum_digits('digits_to_sum.txt')

# Final answer
# import sys
#
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     if line == "":
#         continue
#     else:
#         full_line = ""
#         for num in line:
#             full_line += str(num)
#     full_line = int(full_line)
#     print sum(map(int, str(full_line)))
