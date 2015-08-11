# Print out the sum of integers read from a file.
#
# INPUT SAMPLE:
# The first argument to the program will be a path to a filename containing a positive integer, one per line.
# 5
# 12
#
# OUTPUT SAMPLE:
# Print out the sum of all the integers read from the file. E.g.
# 17

# For Testing    (787091)


# def sum_digits(filename):
#     f = open(filename, 'r+')
#     total = 0
#     for line in f:
#         if line == "":
#             continue
#         else:
#             number = int(line)
#             total += number
#     return total
#
# print sum_digits('digits_to_sum.txt')


# Final answer
# import sys
#
#
# f = open(sys.argv[1], 'r+')
# total = 0
# for line in f:
#     if line == "":
#         continue
#     else:
#         number = int(line)
#         total += number
# print total
