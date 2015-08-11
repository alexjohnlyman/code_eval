# Given an integer n>=0, print out the F(n).
#
# INPUT SAMPLE:
# The first argument will be a path to a filename containing integer numbers, one per line.
# 5
# 12
#
# OUTPUT SAMPLE:
# Print to stdout, the fibonacci number, F(n). E.g.
# 5
# 144

# TESTING
# def fib(file):
#     f = open(file, 'r+')
#     for line in f:
#         a, b = 0, 1
#         x = int(line)
#         for i in range(x):
#             a, b = b, a + b
#         print a
#
# print fib('fib_nums.txt')


# FINAL ANSWER
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     a, b = 0, 1
#     x = int(line)
#     for i in range(x):
#         a, b = b, a + b
#     print a