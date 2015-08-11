# Write a program which determines the sum of the first 1000 prime numbers.
# Print to stdout the sum of the first 1000 prime numbers, or 3682913

# Final Solution(s)
# import math


# def is_prime(num):
#     sq_root = int(math.ceil(math.sqrt(num)))
#     for i in range(2, sq_root + 1):
#         if num % i == 0:
#             return False
#     else:
#         return True



# Alternate is_prime method w/o math


def is_prime(num):
    sq_root = int(num**0.5)+1
    for i in range(2, sq_root + 1):
        if num % i == 0:
            return False
    else:
        return True


def check_up_to(number):
    num_of_primes = 1
    sum_of_primes = 2
    i = 2
    while num_of_primes < number:
        if is_prime(i):
            sum_of_primes += i
            num_of_primes += 1
            i += 1
        else:
            i += 1
    print sum_of_primes

check_up_to(1000)
