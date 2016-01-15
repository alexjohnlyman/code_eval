# Morse code
# You have received a text encoded with Morse code and want to decode it.
# Each letter is separated by space char, each word is separated by 2 space chars.
# You program has to support letters and digits only.

# INPUT SAMPLE:
# .- ...- ..--- .-- .... .. . -.-. -..-  ....- .....
# -... .... ...--

# OUTPUT SAMPLE:
# AV2WHIECX 45
# BH3

# Testing
# my_dict = {'':' ', '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':1, '..---':2, '...--':3, '....-':4, '.....':5, '-....':6, '--...':7, '---..':8, '----.':9, '-----':0}

# def change(file):
# 	with open(file, 'r') as f:
# 		for line in f:
# 			no_return = line.rstrip('\n')
# 			string = no_return.split(" ")
# 			for m,i in enumerate(string):
# 			    if i in my_dict:
# 			        string[m]=my_dict[i]
# 		        print ''.join("{0}".format(n) for n in string)

# change('morsecode.txt')


# Final solution
# import sys

# f = open(sys.argv[1], 'r')
# my_dict = {'':' ', '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':1, '..---':2, '...--':3, '....-':4, '.....':5, '-....':6, '--...':7, '---..':8, '----.':9, '-----':0}

# for line in f:
# 	no_return = line.rstrip('\n')
# 	string = no_return.split(" ")
# 	for m,i in enumerate(string):
# 	    if i in my_dict:
# 	        string[m]=my_dict[i]
#         print ''.join("{0}".format(n) for n in string)


