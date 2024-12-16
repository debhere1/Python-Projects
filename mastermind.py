import random

def get_num():
    guess = int(input("Guess again for remaining digits: "))
    print(guess)

    if 1000 > guess or guess > 9999:
        print("Invalid input. Try again.")
        exit()

    elif guess == actual:
        print("Correct! You are the man")
        exit()

    else:
        compare_guess()

def compare_guess():
    while actual != guess:
        str1 = str(actual)
        str2 = str(guess)

        if str1 == str2:
            print("Correct! You are winner")
            exit()

        # Compare digits
        result = " "
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                result = result + str1[i]
            else:
                result= result + "X"
        print("The digits you got correct are \n:",result)
        print("Try again")
        get_num()
        continue

actual =  random.randint(1000,9999)
print(actual)
result = " "
guess = int(input("Guess the number between 1000 and 9999: "))
if 1000 > guess or guess > 9999:
    print("Invalid input. Try again.")
    exit()
elif guess == actual:
    print("Correct! You are the man")
    exit()
else:
    compare_guess()






