# STEPWISE WORD
# Print the longest word in a stepwise manner.

# INPUT SAMPLE:
# cat dog hello
# stop football play
# music is my life

# The first argument is a path to a file.
# Each line contains a test case with a list of words that have different or the same length.


# OUTPUT SAMPLE:
# h *e **l ***l ****o
# f *o **o ***t ****b *****a ******l *******l
# m *u **s ***i ****c

# Find the longest word in each line and print it in one line in a stepwise manner.
# Separate each new step with a space.
# If there are several words of the same length and they are the longest, then print the first word from the list.


def stepping_words(file):
    with open(file, 'r+') as f:
        for line in f:
            word = line.split()
            word.sort(key=len)
            last_word = word[-1]
            final_word = []
            num_stars_to_add = len(last_word)
            for x in range(0, num_stars_to_add):    # Issues with getting the right number of stars in the right place.
                print x
                # final_word.append(letter)
            print ' '.join(final_word)

stepping_words("stepwise_words.txt")


# def longest_lines(file):
#     with open(file, 'r+') as f:
#         number_of_lines = int(f.readline())
#         sorted_list = sorted(f, key=len, reverse=True)
#         longest_list = []
#         for word in sorted_list:
#             longest_list.append(word.strip('\n'))
#         print '\n'.join(longest_list[0:number_of_lines])


# Final Solution
# import sys

# f = open(sys.argv[1], 'r+')
# number_of_lines = int(f.readline())
# sorted_list = sorted(f, key=len, reverse=True)
# longest_list = []
# for word in sorted_list:
#     longest_list.append(word.strip('\n'))
# print '\n'.join(longest_list[0:number_of_lines])
