# Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not.
# Positions p1 and p2 are 1 based.

# The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line.

# INPUT SAMPLE:
# 86,2,3
# 125,1,2

# OUTPUT SAMPLE:
# true
# false

# Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase).

# Testing - Long
# def bit_pos(file):
#     f = open(file, 'r+')
#     for line in f:
        # number_1 = line.rstrip('\n').split(",")[0]
        # number_2 = line.rstrip('\n').split(",")[1]
        # number_3 = line.rstrip('\n').split(",")[2]
        # number_1_int = int(number_1)
        # number_2_int = int(number_2)
        # number_3_int = int(number_3)
        # num_bin_1 = '{:b}' .format(number_1_int)
        # p1 = num_bin_1[-number_2_int]
        # p2 = num_bin_1[-number_3_int]
#         if p1 == p2:
#             print "true"
#         else:
#             print "false"

# bit_pos("bit_positions.txt")


# Testing - shortened
# def bit_pos(file):
#     f = open(file, 'r+')
#     for line in f:
#         num_bin_1 = '{:b}' .format(int(line.rstrip('\n').split(",")[0]))
#         p1 = num_bin_1[-int(line.rstrip('\n').split(",")[1])]
#         p2 = num_bin_1[-int(line.rstrip('\n').split(",")[2])]
#
#         if p1 == p2:
#             print "true"
#         else:
#             print "false"
#
#
# bit_pos("bit_positions.txt")



# Final Solution

# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     num_bin_1 = '{:b}' .format(int(line.rstrip('\n').split(",")[0]))
#     p1 = num_bin_1[-int(line.rstrip('\n').split(",")[1])]
#     p2 = num_bin_1[-int(line.rstrip('\n').split(",")[2])]
#
#     if p1 == p2:
#         print "true"
#     else:
#         print "false"