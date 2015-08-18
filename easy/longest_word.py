# LONGEST WORD
# In this challenge you need to find the longest word in a sentence.
# If the sentence has more than one word of the same length you should pick the first one.
# Your program should accept as its first argument a path to a filename.
#
# INPUT SAMPLE:
# some line with text
# another line
#
# Each line has one or more words. Each word is separated by space char.
# Print the longest word in the following way.
#
# OUTPUT SAMPLE:
# some
# another

# Testing
# def long_word(file):
#     with open(file, 'r+') as f:
#         for line in f:
#             word = line.split()
#             sort_key = lambda s: (-len(s))
#             word.sort(key=sort_key)
#             print ''.join(word[0:1])
#
# long_word("longest_word.txt")

# Final solution
# import sys
#
# f = open(sys.argv[1], 'r+')
# for line in f:
#     word = line.split()
#     sort_key = lambda s: (-len(s))
#     word.sort(key=sort_key)
#     print ''.join(word[0:1])
