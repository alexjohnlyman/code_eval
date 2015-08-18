# SET INTERSECTION
# You are given two sorted list of numbers (ascending order).
# The lists themselves are comma delimited and the two lists are semicolon delimited.
# Print out the intersection of these two sets.

# File containing two lists of ascending order sorted integers, comma delimited, one per line.

# INPUT SAMPLE:
# 1,2,3,4;4,5,6
# 20,21,22;45,46,47
# 7,8,9;8,9,10,11,12
# 7,8,9,10,11;8,9,10,11,12,13,14,15,16
# 8,9,10,11;8,9,10,11
# 20,21,22;23,24,25,26
# 0,1,2,3,4,5;5,6,7,8

# Print out the ascending order sorted intersection of the two lists, one per line.
# Print empty new line in case the lists have no intersection.

# OUTPUT SAMPLE:
# 4
#
# 8,9
# 8,9,10,11
# 8,9,10,11
#
# 5


# def set_intersect(file):
#     with open(file, 'r+') as f:
#         for line in f:
#             line_divided = line.split(';')
#             first_half = line_divided[0].split(',')
#             second_half = line_divided[1].split(',')
#             set_second = set(second_half)
#             # intersect = sorted((list(set(first_half).intersection(second_half))), key=int)
#             # final_string = ', '.join(intersect)
#             for value in first_half:
#                 if value in set_second:
#                     print value
#                     # if final_string is "":
#                     #     print ""
#                     # else:
#                     #     print final_string
#
#
# set_intersect("set_intersect.txt")



def set_intersect_orig(file):
    with open(file, 'r+') as f:
        for line in f:
            line_divided = line.split(';')
            first_half = line_divided[0].split(',')
            second_half = line_divided[1].split(',')
            second_half = map(str.strip, second_half)
            intersect = sorted((list(set(first_half).intersection(second_half))), key=int)
            final_string = ', '.join(intersect)
            if final_string is "":
                print ""
            else:
                print final_string


set_intersect_orig("set_intersect.txt")


# Final Solution     STILL NEED TO FIX
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     line_divided = line.split(';')
#     first_half = line_divided[0].split(',')
#     second_half = line_divided[1].split(',')
#     intersect = sorted((list(set(first_half).intersection(second_half))), key=int)
#     final_string = ', '.join(intersect)
#     if final_string is "":
#         print ""
#     else:
#         print final_string
