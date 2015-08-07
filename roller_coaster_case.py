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
    input = open(filename, 'r+')
    count = 2
    for line in input:
        for letter in line:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                if count % 2 == 0:
                    letter.upper()
                    count += 1
                elif count % 2 != 0:
                    letter.lower()
                    count += 1
            else:
                continue
    input.close()

    #     if line == "":
    #         continue
    #     else:
    #         new_line = line.lower()
    #         for lower_line in new_line

print stdout('lowercase.txt')

# Final answer
# import sys
#
#
# input = open(sys.argv[1], 'r+')
# for line in input:
#     print line.lower()
