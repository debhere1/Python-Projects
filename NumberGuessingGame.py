import random
import math
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

#guess = random.randint(lower_bound, upper_bound)
actual = random.randint(lower_bound, upper_bound)
max_attempts = math.ceil(math.log2(upper_bound - lower_bound+1))
print("Maximum number of attempts: ", max_attempts)
guess = int(input("Enter guess: "))
count = 1

while count <= max_attempts:
 if guess == actual:
    print("Congratulations! You guessed it right!")
    break
 elif guess > actual:
    print("Sorry, that's too high!",max_attempts-count, "attempts left")
    #upper_bound = guess
    guess = int(input("Enter guess: "))
    count += 1
    if count > max_attempts:
        print("Better luck next time! The actual number is " + str(actual))
        break
 elif guess < actual:
    print("Sorry, that's too low!", max_attempts-count, "attempts left")
    #lower_bound = guess
    guess = int(input("Enter guess: "))
    count += 1
    if count > max_attempts:
        print("Better luck next time! The actual number is " + str(actual))
        break
