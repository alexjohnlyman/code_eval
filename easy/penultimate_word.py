# PENULTIMATE WORD
# Write a program which finds the next-to-last word in a string.

# INPUT SAMPLE:
# some line with text
# another line

# Your program should accept as its first argument a path to a filename.
# Input example is the following
# Each line has more than one word.

# OUTPUT SAMPLE:
# with
# another

# Print the next-to-last word in the following way.


# Testing
# def penultimate_word(file):
#     with open(file, 'r+') as f:
#         for line in f:
#             print ''.join(line.split()[-2:-1:])
#             # Broken down into parts
#                 # line_list = line.split()
#                 # isolated_word = line_list[-2:-1:]
#                 # new_string = ''.join(line.split()[-2:-1:])
#
# penultimate_word("penultimate_word.txt")


# Final Solution
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     print ''.join(line.split()[-2:-1:])
