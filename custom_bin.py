# Converts a base 10 int to its binary form - no use of bin() - - no external module except sys for
# argument passing

#  67                       any positive int n
# [64,               2, 1]  decompose n to an array of its powers of two
# [64, 32, 16, 8, 4, 2, 1]  generate an array of all powers of 2 up to largest power p where p < n
# [X,  O,   O, O, O, X, X]  for every x in array of powers, replace it with X (string) if in decomposed array, else O (string)
# [1,  0,   0, 0, 0, 1, 1]  for every x in array last array, replace X with 1 and O with 0
# 1000011

# write tests for it

import sys

class Converter:

    def convert(self, number):
        decomposed = self.decompose(number)
        powersOfTwo = self.generatePowersOfTwo(number)
        for i in range(len(powersOfTwo)):
            powersOfTwo[i] = "X" if powersOfTwo[i] in decomposed else "O"
        for i in range(len(powersOfTwo)):
            powersOfTwo[i] = "1" if powersOfTwo[i] == "X" else "0"
        result = powersOfTwo
        result = "".join([str(x) for x in result])
        return int(result)

    # int --> [] | [...]
    def decompose(self, number):
        """ Decomposes any int to a list of its powers of two. Returns an empty list if none is found """
        powersOfTwo = []
        while self.findLargestPowerOfTwo(number) is not False:
            largestPowerOfTwo = self.findLargestPowerOfTwo(number)
            powersOfTwo.append(largestPowerOfTwo)
            number -= largestPowerOfTwo
        return powersOfTwo

    def generatePowersOfTwo(self, maximum):
        """ generate an array of all powers of 2 starting from 1 up to 'startFrom' """
        maximum = self.binaryLog(maximum)
        powersOfTwo = []
        for i in range(maximum + 1):
            powersOfTwo.append(2 ** i)
            i -= 1
        powersOfTwo.reverse()
        return powersOfTwo

    # for any integer N, finds the largest power p of 2 where p <= N
    # int --> False | int
    def findLargestPowerOfTwo(self, n):
        if n <= 0: return False
        p = n
        while not self.isPowerOfTwo(p) and not p < 0:
            p = p - 1
        return False if p < 0 else p

    # int --> True | False
    def isPowerOfTwo(self, n):
        if n!= 2:
            if n == 1: return True
            return self.isPowerOfTwo(n / 2) if (n / 2) % 2 == 0 else False
        else:
            return True

    def binaryLog(self, n):
        """ any power of two --> int """
        power = 0
        while n >= 2:
            n = n / 2
            power += 1
        return power

if __name__ == "__main__":
    converter = Converter()
    try:
        input = int(sys.argv[1])
    except (IndexError, ValueError):
        input = int(input("Veuillez entrer un nombre à convertir : "))
    print(converter.convert(input))
