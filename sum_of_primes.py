# Write a program which determines the sum of the first 1000 prime numbers.
# Print to stdout the sum of the first 1000 prime numbers, or 3682913

# I need to add to the counter only after a number is confirmed prime.

primes = []


def stdout():
    count = 3
    while len(primes) < 200:
        for y in range(2, count + 1):
            for i in range(2, count):
                if (y % i) == 0:
                    break
            else:
                primes.append(count)
        count += 1
    return primes

print stdout()




# prime_palin = []
#
# def stdout():
#     for num in range(3, 1001):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             palindrome(num)
#     return prime_palin[-1]
#
#
# def palindrome(y):
#     y = str(y)
#     if y[0] == y[-1]:
#         prime_palin.append(y)
#     return prime_palin
#
# print stdout()