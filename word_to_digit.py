# Having a string representation of a set of numbers you need to print this numbers.

# All numbers are separated by semicolon. There are up to 20 numbers in one line.
# The numbers are "zero" to "nine".

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename.
# Each line in this file is one test case.

# zero;two;five;seven;eight;four
# three;seven;eight;nine;two

# OUTPUT SAMPLE:
# Print numbers in the following way:

# 025784
# 37892

# test = ("zero", "two", "five", "seven", "eight", "four")
# my_dict = {'zero:0', 'one:1', 'two:2', 'three:3', 'four:4', 'five:5', 'six:6', 'seven:7', 'eight:8', 'nine:9'}
#
#
# def replace_all(text, my_dict):
#     for text, number in my_dict:
#         text = text.replace(text, number)
#     return text
#
#
# def change(filename):
#     with open(filename, 'r') as in_file:
#         text = in_file.read()
#     with open() as out_file:
#         out_file.write(replace_all(text, my_dict))
#
# print change('test_file.txt')
