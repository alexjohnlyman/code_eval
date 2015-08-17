# You are given 3 coins of value 1, 3 and 5.
# You are also given a total which you have to arrive at.
# Find the minimum number of coins to arrive at it.

# INPUT SAMPLE:
# 2
# 4
# 8
# 11
# 14
# 21
# 35


# Your program should accept as its first argument a path to a filename.
# Each line in this file represents the total you have to arrive at.

# OUTPUT SAMPLE:
# 2
# 2
# 2
# 3
# 4
# 5
# 7

# Print out the minimum number of coins required to arrive at the total.

# Testing - 2
# def minimum_coins(file):
#     f = open(file, 'r+')
#     for line in f:
#         line = int(line)
#         ints = (5, 3, 1)
#         total = 0
#         for i in range(len(ints)):
#             count = int(line / ints[i])
#             total += count
#             line -= ints[i] * count
#         print total
#
# minimum_coins("minimum_coins.txt")


# Testing - this needs to be refactored
# def minimum_coins(file):
#     f = open(file, 'r+')
#     for line in f:
#         num_of_coins = 0
#         line = int(line)
#         div_5 = line / 5
#         left_after_5 = line % 5
#         num_of_coins += div_5
#         if line == 0:
#             print 0
#             continue
#         elif left_after_5 == 0:
#             print num_of_coins
#             break
#         elif left_after_5 < 3:
#             num_of_coins += left_after_5
#         else:
#             if left_after_5 == 3:
#                 num_of_coins += 1
#             else:
#                 num_of_coins += 2
#         print "Line number is: {}" .format(line)
#         print "Coins used: {}" .format(num_of_coins)
#
#
# minimum_coins("minimum_coins.txt")


# Final Solution - Still not complete. Need to work on this some more.
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     num_of_coins = 0
#     line = int(line)
#     div_5 = line / 5
#     left_after_5 = line % 5
#     num_of_coins += div_5
#     if line == 0:
#         print 0
#         continue
#     elif left_after_5 == 0:
#         print num_of_coins
#         break
#     elif left_after_5 < 3:
#         num_of_coins += left_after_5
#     else:
#         if left_after_5 == 3:
#             num_of_coins += 1
#         else:
#             num_of_coins += 2
#     print num_of_coins


# Final Solution - 2
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     line = int(line)
#     ints = (5, 3, 1)
#     total = 0
#     for i in range(len(ints)):
#         count = int(line / ints[i])
#         total += count
#         line -= ints[i] * count
#     print total
