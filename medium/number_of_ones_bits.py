# A program determines the number of 1 bits in a given integer.

# INPUT SAMPLE:
# 10
# 22
# 56
# 80
# 111
# 370

# The first argument is a path to a file.
# The file contains integers, one per line.

# OUTPUT SAMPLE:
# 2
# 3
# 3
# 2
# 6
# 5

# Print to stdout the number of ones in the binary form of each number.


# Testing
# def bit_pos(file):
#     f = open(file, 'r+')
#     for line in f:
#         num_bin = '{:b}' .format(int(line))
#         count_ones = 0
#         for i in num_bin:
#             if i == "1":
#                 count_ones += 1
#         print count_ones
#
# bit_pos("number_of_ones.txt")


# Final Solution

# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     num_bin = '{:b}' .format(int(line))
#     count_ones = 0
#     for i in num_bin:
#         if i == "1":
#             count_ones += 1
#     print count_ones