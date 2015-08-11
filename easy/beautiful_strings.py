# Given a string s, the beauty of the string as the sum of the beauty of the letters in it.
# The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty.
# Uppercase 'F' is exactly as beautiful as lowercase 'f'.

# Your program should accept as its first argument a path to a filename.
# Each line in this file has a sentence.

# INPUT SAMPLE:
# ABbCcc
# Good luck in the Facebook Hacker Cup this year!
# Ignore punctuation, please :)
# Sometimes test cases are hard to make up.
# So I just go consult Professor Dalves

# Print out the maximum beauty for the string.
# OUTPUT SAMPLE:
# 152
# 754
# 491
# 729
# 646


# Testing  (reading lines from a file, counting them and placing them in arrays)

# def convert_str(sentence):
#     only_alpha = ""
#     sentence = sentence.replace(" ", "")
#     sentence = sentence.strip()
#     sentence = sentence.lower()
#     for x in sentence:
#         if x.isalpha():
#             only_alpha += x
#     return only_alpha
#
#
# def beautiful_str(file):
#     f = open(file, 'r+')
#     for sentence in f:
#         line = convert_str(sentence)
#         count = dict()
#         for i in line:
#             if i in line:
#                 count[i] = count.get(i, 0) + 1
#         sorted_dict = sorted(count.values())
#         reverse_list = sorted_dict[::-1]
#         amount_per_letter = 26
#         beautiful_total = 0
#         for x in reverse_list:
#             beautiful_total += x*amount_per_letter
#             amount_per_letter -= 1
#         print beautiful_total
#
# beautiful_str("beautiful_str.txt")


# Final solution - Could probably be refactored some more

# import sys
#
#
# def convert_str(sentence):
#     only_alpha = ""
#     sentence = sentence.replace(" ", "")
#     sentence = sentence.strip()
#     sentence = sentence.lower()
#     for x in sentence:
#         if x.isalpha():
#             only_alpha += x
#     return only_alpha
#
#
# f = open(sys.argv[1], 'r+')
# for sentence in f:
#     line = convert_str(sentence)
#     count = dict()
#     for i in line:
#         if i in line:
#             count[i] = count.get(i, 0) + 1
#     sorted_dict = sorted(count.values())
#     reverse_list = sorted_dict[::-1]
#     amount_per_letter = 26
#     beautiful_total = 0
#     for x in reverse_list:
#         beautiful_total += x*amount_per_letter
#         amount_per_letter -= 1
#     print beautiful_total
