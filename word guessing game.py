import random
import requests

words = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood",
             "Board", "Brain", "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief",
             "Child", "China", "Claim", "Class", "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime",
             "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft", "Drama", "Dream",
             "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry"]

word = words[random.randint(0, len(words) - 1)]

tries = 6

while tries > 0:

    guess = input("Enter your guess: ")
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{guess}")
    if response.status_code != 200:
        print(f"'{guess}' is not a valid word. Please try again.")
        continue
    if guess == word:
        print("Correct! You won the game.")
        break

    feedback = ""
    for i in range(len(guess)):
        if guess[i] == word[i]:
            feedback += guess[i]
        else:
            feedback += "_"
    print("Feedback: ", feedback)
    tries -= 1

if tries == 0:
    print("Sorry, you have used up all your tries. The word was '" + word + "'.")
