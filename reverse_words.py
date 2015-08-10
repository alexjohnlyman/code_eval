# INPUT SAMPLE:
# The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.
#
# For example:
# Hello World
# Hello CodeEval

# OUTPUT SAMPLE:
# Print to stdout each sentence with the reversed words in it, one per line.
# Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.
#
# For example:
# World Hello
# CodeEval Hello


# TESTING
# def stdout(file_name):
#     with open(file_name, 'r+') as f:
#         divide_lines = f.readlines()
#         for line in divide_lines:
#             words = line.split()
#             reverse_words = words[::-1]
#             x = ' '.join(reverse_words)
#             print x
#
# stdout('words.txt')



# FINAL ANSWER
# import sys

# f = open(sys.argv[1], 'r+')
# divide_lines = f.readlines()
# for line in divide_lines:
#     words = line.split()
#     reverse_words = words[::-1]
#     x = ' '.join(reverse_words)
#     print x

