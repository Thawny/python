import sys

def add(a,b):
    return int(a) + int(b)

try:
    print(add(sys.argv[1], sys.argv[2]))
except IndexError:
    input = int(input("Nombre d'arguments insuffisant, veuillez entrez un chiffre"))
    inp2 = int(input("veuillez entrez un deuxième chiffre"))
print("Hello")
