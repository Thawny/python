import random

randInt = random.randint(1,100)

def play(counter):
    if counter != 0:
        guess = int(input('Choisissez un nombre entre 1 et 100\n'))
        if guess < randInt:
            print(guess, " est trop petit")
            play(counter - 1)
        elif guess > randInt:
            print(guess, " est trop grand")
            play(counter - 1)
        else:
            print('Bravo! Vous avez gagné, la réponse était bien ', randInt)
    else:
        print('Désolé, vous avez épuisé vos chances, la réponse était ', randInt)


play(6)
