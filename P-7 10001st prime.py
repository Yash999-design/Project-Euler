#! Version 1 : takes a lot of time

# import time

# def is_prime_v1(n):
#    """Return 'True' if 'n' is a prime number. False otherwise."""
#     if n == 1:
#         return False  #! 1 is not prime

#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     return True


# #! ========= Test Function =========
# # for n in range(1, 21):
# #     print(n, is_prime_v1(n))

# #! =========== Time Function ==========
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v1(n)
# t1 = time.time()
# print("Time required : ", t1 - t0)


#! Version 2 : Reduce number of divisors we check in the for loop
# import math
# import time


# def is_prime_v2(n):
#     """Return 'True' if 'n' is a prime number. False otherwise."""
#     if n == 1:
#         return False #! 1 is not prime

#     max_divisor = math.floor(math.sqrt(n))
#     for d in range(2, 1 + max_divisor):
#         if n % d == 0:
#             return False
#     return True

# # #* =========== Test Function =============
# # for n in range(1, 21):
# #     print(n, is_prime_v2(n))

# #! =========== Time Function ==========
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v2(n)
# t1 = time.time()
# print("Time required : ", t1 - t0)


# #! Version - 3 : It's a waste to check even numbers. So we only check odd divisors

# import math
# import time


# def is_prime_v3(n):
#     """Return 'True' if 'n' is a prime number. False otherwise."""
#     if n == 1:
#         return False #! 1 is not prime

#     #! If it' even and not 2, then it's not prime
#     if n == 2: #2 is a prime number
#         return True
#     if n > 2 and n % 2 == 0:
#         return False

#     max_divisor = math.floor(math.sqrt(n))
#     for d in range(3, 1 + max_divisor, 2):
#         if n % d == 0:
#             return False
#     return True

# #* =========== Test Function =============
# for n in range(1, 21):
#     print(n, is_prime_v3(n))

# #! =========== Time Function ==========
# t0 = time.time()
# for n in range(1, 1000000):
#     is_prime_v3(n)
# t1 = time.time()
# print("Time required : ", t1 - t0)


# ? Solution of my problem


import math
import time


def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False  # ! 1 is not prime

    #! If it' even and not 2, then it's not prime
    if n == 2:  # 2 is a prime number
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# * =========== Test Function =============


l1 = []
for n in range(1, 1000000):
    # print(n, is_prime_v3(n))
    if is_prime_v3(n) == True:
        l1.append(n)

print(l1[10000])
