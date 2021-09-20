import random

def main():

    num = random.random()
    favourite = "bats"
    if num < 0.2:
        if num < 0.1:
            favourite = 'cats'
        else:
            favourite = 'bats'
    else:
        favourite = 'dogs'
    print("I love " + favourite) 


main()

