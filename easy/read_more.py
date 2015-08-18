# READ MORE
# If line length is <= 55 characters, print it without any changes.
# If the line length is > 55 characters, change it as follows:
# Trim the line to 40 characters.
# If there are spaces ' ' in the resulting string, trim it once again to the last space (the space should be trimmed).
# Add a string '... <Read More>' to the end of the resulting string and print it.
# The first argument is a file. The file contains a text.
#
#
# INPUT SAMPLE:
#
# Tom exhibited.
# Amy Lawrence was proud and glad, and she tried to make Tom see it
# in her face - but he wouldn't look.
# Tom was tugging at a button-hole and looking sheepish.
# Two thousand verses is a great many - very, very great many.
# Tom's mouth watered for the apple, but he stuck to his work.
#
# Print the text lines with their length limited according to the rules described above.
#
# OUTPUT SAMPLE:
#
# Tom exhibited.
# Amy Lawrence was proud and glad, and... <Read More>
# Tom was tugging at a button-hole and looking sheepish.
# Two thousand verses is a great many -... <Read More>
# Tom's mouth watered for the apple, but... <Read More>
#
# CONSTRAINTS:
# The maximum length of a line in the input file is 300 characters.
# There cannot be more than one consequent space character in the input data.


def read_more(file):
    with open(file, 'r+') as f:
        for line in f:
            if line == "":
                continue
            elif len(line) <= 55:
                print line
            else:
                first_part = line[0:40].rsplit(' ', 1)[0]
                second_part = "... <Read more>"
                print "{}{}" .format(first_part, second_part)

read_more("read_more.txt")
