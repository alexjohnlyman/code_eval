# Write a program that sets the case of text characters according to the following rules:
#
# The first letter of the line should be in uppercase.
# The next letter should be in lowercase.
# The next letter should be in uppercase, and so on.
# Any characters, except for the letters, are ignored during determination of letter case.

# INPUT SAMPLE
# The first argument will be a path to a filename containing sentences, one per line.
# You can assume that all characters are from the English language.

# To be, or not to be: that is the question.
# Whether 'tis nobler in the mind to suffer.
# The slings and arrows of outrageous fortune.
# Or to take arms against a sea of troubles.
# And by opposing end them, to die: to sleep.

# OUTPUT SAMPLE
# Print to stdout the RoLlErCoAsTeR case version of the string.

# To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
# WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR.
# ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE.
# Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS.
# AnD bY oPpOsInG eNd ThEm, To DiE: tO sLeEp.

# The length of each piece of text does not exceed 1000 characters.


# Testing
def stdout(filename):
    f = open(filename, 'r+')
    for line in f:
        letter_count = 1
        full_line = ""
        for letter in line:
            letter = letter.lower()
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                letter_count += 1
                if letter_count % 2 == 0:
                    full_line += letter.upper()
                else:
                    full_line += letter.lower()
            else:
                full_line += letter
        print full_line

stdout('lowercase.txt')


# Final answer
import sys

f = open(sys.argv[1], 'r+')
for line in f:
    letter_count = 1
    full_line = ""
    for letter in line:
        letter = letter.lower()
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            letter_count += 1
            if letter_count % 2 == 0:
                full_line += letter.upper()
            else:
                full_line += letter.lower()
        else:
            full_line += letter
    print full_line
