# An Armstrong number: the sum of the n'th powers(based on number of digits) which sum equals the number itself.
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

# These numbers should return true:
# 153
# 370
# 371
# 407

# Testing 1

# test = 153
# def armstrong(number):
#     convert_number = str(number)
#     power = len(convert_number)
#     total = 0
#     for num in convert_number:
#         raised = pow(int(num), power)
#         total += raised
#     return total
#
# print armstrong(test)

# Testing 2 - added True/False output

# def armstrong(file):
#     f = open(file, 'r+')
#     for line in f:
#         number = int(line)
#         split_number = line.split()
#         convert_number = str(split_number)
#         power = len(str(convert_number))-4
#         total = 0
#         for num in convert_number:
#             if num is "[" or num is "]" or num is "'":
#                 continue
#             else:
#                 raised = pow(int(num), power)
#                 total += raised
#         if total == number:
#             print True
#         else:
#             print False
# armstrong('numbers_armstrong.txt')


# Refactoring of solution


# def armstrong(file):
#     f = open(file, 'r+')
#     for line in f:
#         number = int(line.lstrip('[]'))
#         convert_number = str(line.split())
#         power = len(str(convert_number))-4
#         total = 0
#         for num in convert_number:
#             if num is "[" or num is "]" or num is "'":
#                 continue
#             else:
#                 raised = pow(int(num), power)
#                 total += raised
#         if total == number:
#             print True
#         else:
#             print False
# armstrong('numbers_armstrong.txt')


# Final Solution

# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#         number = int(line)
#         split_number = line.split()
#         convert_number = str(split_number)
#         power = len(str(convert_number))-4
#         total = 0
#         for num in convert_number:
#             if num is "[" or num is "]" or num is "'":
#                 continue
#             else:
#                 raised = pow(int(num), power)
#                 total += raised
#         if total == number:
#             print True
#         else:
#             print False