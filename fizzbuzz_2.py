def divisibility(n):
    return (not n % 2, not n % 3)

def whichfizz(divisibility, n):
    if divisibility == (True, False):
        return 'Fizz'
    elif divisibility == (False, True):
        return 'Buzz'
    elif divisibility == (True, True):
        return 'FizzBuzz'
    else:
        return n

def main():
    print([whichfizz(divisibility(n),n) for n in range(1,20)])

if __name__ == "__main__":
    main()
