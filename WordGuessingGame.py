import random

name = input("What is your name? ")
print("Good luck, " + name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the letters:")

guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
          if char in guesses:
              print(char, end=" ")

          else:
              print("_")
              failed += 1

    if  failed == 0:
        print("You guessed the correct word!", "It is", word)
        break

    guess = input("Enter the letters: ")
    guesses += guess

    if guess not in word:
      turns -= 1
      print("Wrong! You have", turns, "turns left.")

    if turns == 0:
      print("Incorrect. You lose. Correct word is", word)
