# ROMAN NUMERALS

# I - 1
# IV - 4
# V - 5
# IX - 9
# X - 10
# XL - 40
# L - 50
# XC - 90
# C - 100
# CD - 400
# D - 500
# CM - 900
# M  - 1000

# The exceptions to this rule occur for numbers having units values of 4 or 9, and for tens values of 40 or 90.
# For these cases, the Roman numeral representations are IV (4), IX (9), XL (40), and XC (90).
# So the Roman numeral representations for 24, 39, 44, 49, and 94 are XXIV, XXXIX, XLIV, XLIX, and XCIV, respectively.

# Write a program to convert a cardinal number to a Roman numeral. Input numbers are in range [1, 3999]

# INPUT SAMPLE:
# 15
# 24
# 73
# 159
# 296
# 3992

# OUTPUT SAMPLE:
# XV
# XXIV
# LXXIII
# CLIX
# CCXCVI
# MMMCMXCII

# Expanded solution with error handling
# def roman_nums(file):
#     with open(file, 'r+') as f:
#         for line in f:
#             line = int(line)
#             if not isinstance(line, type(1)):
#                 raise TypeError, "expected integer, got %s" % type(line)
#             if not 0 < line < 4000:
#                 raise ValueError, "Argument must be between 1 and 3999"
#             ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
#             nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
#             result = []
#             for i in range(len(ints)):
#                 count = int(line / ints[i])
#                 result.append(nums[i] * count)
#                 line -= ints[i] * count
#             print ''.join(result)
#
# roman_nums("roman_numerals.txt")


def roman_nums(file):
    with open(file, 'r+') as f:
        for line in f:
            line = int(line)
            ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
            nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
            result = []
            for i in range(len(ints)):
                count = int(line / ints[i])
                result.append(nums[i] * count)
                line -= ints[i] * count
            print ''.join(result)

roman_nums("roman_numerals.txt")
