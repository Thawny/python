
def scope():
    u = 10
    for i in range(0,5):
        u = u + 1
        print(u)

# scope()

def convert(number):
    while number > 0:
        number -= 2
        print(number)
    print(number, "final")

convert(10)
