# Guess the words
# Created by Ding Zhihao
from random import randint

choices = ["Kitchen", "Garden", "Living Room", "Bathroom"]
print(choices)
chooseTopic = str(input("Choose a topic to connect to: ")).strip().title()


if chooseTopic == "Kitchen":
    words = ["Knife", "Pot", "Refrigerator", "Spoon", "Fork", "Oven", "Microwave", "Table", "Chair", "Pan"]
    print(words)
    computer = words[randint(0, 9)]
    
    for attempts in range(3):
        print("Welcome to the kitchen, guess the word about the kitchen!")
        guess_word = str(input("Please enter your guess: ")).strip().capitalize()

        if guess_word == computer:
            print("Correct")
            break

        else: 
            if guess_word != computer:
                print("Invalid Guess!")

        if attempts == 2: 
            print("Game Over!")
        attempts += 1
            


elif chooseTopic == "Garden":
    words = ["Grass", "Flower", "Pot", "Water", "Lawn mower", "Shovel", "Seed", "Plant", "Soil", "Tree"]
    print(words)
    computer = words[randint(0, 9)]

    for attempts in range(3):
        print("Welcome to the garden, guess the word about the garden!")
        guess_word = str(input("Please enter your guess: ")).strip().capitalize()

        if guess_word == computer: 
            print("Correct!")
            break

        else:
            if guess_word != computer: 
                print("Invalid Guess!")

        if attempts == 2:
            print("Game Over!")
        attempts += 1

elif chooseTopic == "Living Room":
    words = ["Sofa", "TV", "Carpet", "TV Remote", "Book", "Pillow", "Table", "Chair", "Painting", "Clock"]
    print(words)
    computer = words[randint(0, 9)]

    for attempts in range(3):
        print("Welcome to the living room, guess the word about the living room!")
        guess_word = str(input("Please enter your guess: ")).strip().title()

        if guess_word == computer: 
            print("Correct!")
            break

        else:
            if guess_word != computer:
                print("Invalid Guess!")

        if attempts == 2:
            print("Game Over!")
        attempts += 1

elif chooseTopic == "Bathroom":
    words = ["Bathtub", "Toilet", "Sink", "Shower", "Towel", "Soap", "Shampoo", "Hair Dryer", "Clothes", "Alcohol"]
    print(words)
    computer = words[randint(0, 9)]

    for attempts in range(3):
        print("Welcome to the bathroom, guess the word about the bathroom!")
        guess_word = str(input("Please enter your guess: ")).strip().title()

        if guess_word == computer: 
            print("Correct!")
            break

        else:
            if guess_word != computer:
                print("Invalid Guess!")

        if attempts == 2:
            print("Game Over!")
        attempts += 1

else: 
    print("Invalid topic, choose a topic from the following!")