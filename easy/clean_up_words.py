# Given a list of words.
# Letters of these words are mixed with extra symbols, so it is hard to define the beginning and end of each word.
# Write a program that will clean up the words from extra numbers and symbols.
#
# INPUT SAMPLE:
# (--9Hello----World...--)
# Can 0$9 ---you~
# 13What213are;11you-123+138doing7
# 89h2d@fn89c12n$8d9n8j9^82jhn8f*
#
# The first argument is a path to a file. Each line includes a test case with a list of words:
# letters are both lowercase and uppercase, and are mixed with extra symbols.
#
# OUTPUT SAMPLE:
# hello world
# can you
# what are you doing
# h d fn c n d n j jhn f
#
# Print the cleaned up words separated by spaces in lowercase letters.
#
# CONSTRAINTS:
#
# Print the words separated by spaces in lowercase letters.
# The length of a test case together with extra symbols can be in a range from 10 to 100 symbols.
# The number of test cases is 40.


# testing

# import re


# Using regrex
# def clean_up_words_2(file):
#     f = open(file, 'r+')
#     file = f.readlines()
#     for line in file:
#         only_letters = re.sub('[^a-zA-Z]', ' ', line,)
#         final = re.sub(r'\s+', ' ', only_letters)
#         final = final.strip().lower()
#         print final
#
# clean_up_words_2("clean_up_words.txt")


#  no_nums = re.sub('[0-9]', '', line,)
# print no_nums

# whitespace = re.sub('[\s]', '', line)
# print whitespace




# Final solution
# import sys
# import re
#
#
# f = open(sys.argv[1], 'r+')
# file = f.readlines()
# for line in file:
#     only_letters = re.sub('[^a-zA-Z]', ' ', line,)
#     final = re.sub(r'\s+', ' ', only_letters)
#     final = final.strip().lower()
#     print final