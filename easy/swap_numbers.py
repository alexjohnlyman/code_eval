# Swap Numbers

# Given a sentence where each word has a single digit positive integer as a prefix and suffix, 
# swaps the numbers while retaining the word in between. 
# Words in the sentence are delimited from each other by a space.
# Each line of the input file contains one test case represented by a sentence. 
# print to standard output the sentence obtained by swapping the numbers surrounding each word, one per line.

# The suffix and the prefix of each word may be equal.
# Sentences form 1 to 17 words long.
# The number of test cases is 40.

# INPUT SAMPLE:
# 4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
# 5Nobody5 7expects3 5the4 6Spanish4 9inquisition0

# OUTPUT SAMPLE:
# 0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5
# 5Nobody5 3expects7 4the5 4Spanish6 0inquisition9


# Testing
import re


# def switch_numbers (word):
# 	numbers = re.findall('\d+', word)
# 	word = ''.join([i for i in word if i.isalpha()])
# 	new_word = numbers[1] + word + numbers[0]
# 	return new_word


def swap_numbers(file):
	with open(file, 'r') as f:
		for line in f:
			new_line = []
			old_line = line.split()
			for word in old_line:
				numbers = re.findall('\d+', word)
				word = ''.join([i for i in word if i.isalpha()])
				new_word = numbers[1] + word + numbers[0]
				new_line.append(new_word)
			print ' '.join(new_line)

swap_numbers("swapnumbers.txt")



# Final solution
import sys
import re

f = open(sys.argv[1], 'r')
for line in f:
	new_line = []
	old_line = line.split()
	for word in old_line:
		numbers = re.findall('\d+', word)
		word = ''.join([i for i in word if i.isalpha()])
		new_word = numbers[1] + word + numbers[0]
		new_line.append(new_word)
	print ' '.join(new_line)

