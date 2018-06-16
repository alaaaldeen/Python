
import time
import math

def is_prime(n):
    """Return 'Trure' if 'n' is a prime number, 'False' otherwise."""
    if n == 1:
        return False   # 1 is not prime it's unit
    # if it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    # d values above sqrt(n) will give same results for d values under sqrt(n)
    max_divisor = int(math.floor(math.sqrt(n))) # int for py V2
    for d in range(3, 1 + max_divisor, 2):    # 2 steps to exclude the even d
        if n % d == 0:
            return False
    return True

# ------ Time Function ------

t0 = time.time()
for i in range (1, 1000):
    print i, is_prime(i)
t1 = time.time()
print "Time required: ",(t1 - t0)
