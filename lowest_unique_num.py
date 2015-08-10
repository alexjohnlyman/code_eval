# There is a game where each player picks a number from 1 to 9.
# A player wins if his number is the lowest unique.
# We may have 10-20 players in our game.

# Your program should accept as its first argument a path to a filename.

# INPUT SAMPLE:
# 3 3 9 1 6 5 8 1 5 3
# 9 2 9 9 1 8 8 8 2 1 1

# Print a winner's position or 0 in case there is no winner.
# In the first line of input sample the lowest unique number is 6.
# So player 5 wins.

# OUTPUT SAMPLE:
# Print position, not number
# 5
# 0

# Testing - 1 (counting elements and placing them into an array)

# test = [3,3,9,1,6,5,8,1,5,3]
#
# def low_unique_num():
#     count = dict()
#     for i in test:
#         if i in test:
#             count[i] = count.get(i, 0) + 1
#     print count
#
#     # for i in test:
#     #     print i
#
# low_unique_num()


# Testing - 2 (reading lines from a file, counting them and placing them in arrays)
def low_unique_num(file):
    f = open(file, 'r+')
    for line in f:
        count = dict()
        line = line.replace(" ", "")
        line = line.strip()
        for i in line:
            if i in line:
                count[i] = count.get(i, 0) + 1
        # print count
        lowest_single_list = []
        for key, value in count.iteritems():
            lowest = 1
            if value == lowest:
                # print key
                lowest_single_list.append(key)
        print lowest_single_list
        if lowest_single_list == []:
            print '0'
        else:
            print min(lowest_single_list)


low_unique_num("list_of_nums.txt")
