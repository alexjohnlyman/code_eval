# PRIME NUMBERS

# Print out the prime numbers less than a given number N.
# For bonus points your solution should run in N*(log(N)) time or better.
# You may assume that N is always a positive integer.

# Your program should accept as its first argument a path to a filename. Each line in this file is one test case.
# Each test case will contain an integer n < 4,294,967,295.

# INPUT SAMPLE:
# 10
# 20
# 100

# OUTPUT SAMPLE:
# 2,3,5,7
# 2,3,5,7,11,13,17,19
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97

# For each line of input, print out the prime numbers less than N, in ascending order, comma delimited.
# There should not be any spaces between the comma and numbers


# def prime_numbers():
    # with open(file, 'r+') as f:
    #     for line in f:
    #         numbers = set(range(int(line), 1, -1))
    #         primes = []
    #         while numbers:
    #             p = numbers.pop()
    #             primes.append(p)
    #             numbers.difference_update(set(range(p*2, int(line)+1, p)))
    #         sorted_primes =  sorted(primes)
    #         print ', '.join(map(str, sorted_primes))
    # n = 25000
    # numbers = set(range(int(n), 1, -1))
    # primes = []
    # while numbers:
    #     p = numbers.pop()
    #     primes.append(p)
    #     numbers.difference_update(set(range(p*2, int(n)+1, p)))
    #     # print p
    # sorted_primes =  sorted(primes)
    # print ','.join(map(str, sorted_primes))



# OLD
# with open(file, 'r+') as f:
#     num = 1100
#     list_of_primes = [2,]
#     for i in range(2, num):
#         if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
#             if num in list_of_primes:
#                 continue
#             else:
#                 list_of_primes.append(num)
#         else:
#             continue
#     for line in f:
#         stop_number = int(line)
#         primes_per_line = []
#         for i in list_of_primes:
#             if i < stop_number:
#                 primes_per_line.append(i)
#         print ', '.join(map(str, primes_per_line))


# prime_numbers("prime_numbers.txt")
# prime_numbers()
