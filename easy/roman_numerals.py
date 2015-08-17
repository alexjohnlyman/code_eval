# ROMAN NUMERALS

# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
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


def roman_nums(file):
    with open(file, 'r+') as f:
        for line in f:
            print line

roman_nums("roman_numerals.txt")
