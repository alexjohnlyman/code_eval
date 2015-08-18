# HEX TO DECIMAL
# You will be given a hexadecimal (base 16) number.
# Convert it into decimal (base 10).

# Your program should accept as its first argument a path to a filename.
# Each line in this file contains a hex number.
# You may assume that the hex number does not have the leading 'Ox'.
# Also all alpha characters (a through f) in the input will be in lowercase.

# INPUT SAMPLE:
# 9f
# 11
# 64
# C8
# 12C

# Print out the equivalent decimal number.

# OUTPUT SAMPLE:
# 159
# 17
# 100
# 200
# 300


# def hex_to_dec(filename):
#     f = open(filename, 'r+')
#     for line in f:
#         line = line.strip('\n')
#         print int(line, 16)
#
# hex_to_dec("hex_to_decimal.txt")


# Convert decimal to hex
# test = 17
# test_2 = 100
# test_3 = 200
# test_4 = 300
#
#
# def hex_to_dec(num):
#     print hex(num)

#Eliminates 0x from hex number
# def hex_to_dec(num):
#     print hex(num).split('x')[1]
#
# hex_to_dec(test)
# hex_to_dec(test_2)
# hex_to_dec(test_3)
# hex_to_dec(test_4)
