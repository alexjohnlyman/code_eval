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

def reverse_words(file_name):
    with open(file_name, 'r+') as f:
        line = f.read()
        words = line.split()
        # print line[::-1]
        print words
        # for phrase in line:
        #     print phrase
        #     for word in phrase:
        #         words = line.split()
        #         print phrase[::-1]


reverse_words('words.txt')


