# You are given a string 'S' and a character 't'.
# Print out the position of the rightmost occurrence of 't' (case matters) in 'S', print -1 if there is none.

# INPUT SAMPLE:
# Hello World,r
# Hello CodeEval,E

# The first argument will ba a path to a filename, containing a string and a character, comma delimited, one per line.
# Ignore all empty lines in the input file.

# OUTPUT SAMPLE:
# 8
# 10

# Print out the zero based position of the character 't' in string 'S', one per line.
# Do NOT print out empty lines between your output.

# Testing
def rightmost_char(file):
    f = open(file, 'r+')
    for line in f:
        a = line.split(',')
        phrase_to_search = a[0]
        to_find = a[1]
        for letter in phrase_to_search:
            if letter in to_find:
                final_index = phrase_to_search.rfind(letter)
                break
            else:
                final_index = "-1"
        print final_index


rightmost_char("right_chars.txt")


# Final Answer
import sys

f = open(sys.argv[1], 'r+')
for line in f:
    a = line.split(',')
    phrase_to_search = a[0]
    to_find = a[1]
    for letter in phrase_to_search:
        if letter in to_find:
            final_index = phrase_to_search.rfind(letter)
            break
        else:
            final_index = "-1"
    print final_index