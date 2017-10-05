# Trouver tous les multiples de 3 et 5 < n et les additionner

# Int --> Bool
def isMultipleOfThreeFive(number):
    return not (number % 5) or not (number % 3)
