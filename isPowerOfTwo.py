def isPowerOfTwo(n):
    while n != 2:
        if (n / 2) % 2 == 0:
            n = n / 2
            continue
        else:
            return False
    return True

def recursiveIsPowerOfTwo(n):
    if n!= 2:
        res = recursiveIsPowerOfTwo(n / 2) if (n / 2) % 2 == 0 else False
        return res
    else: return True


# n where type of log2(n) is int --> int
def binaryLog(n, m):
    count = 0
    while m is not 10:
        m += 1
        n = n / 2
        count += 1
    return (count, n)

print(binaryLog(64, 1))
