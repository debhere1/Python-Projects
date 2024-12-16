# Function to calculate the sum of all numbers from 1 to n
def sum_of_numbers(n):
    return n * (n + 1) // 2

# Accepting user input
num = int(input("Enter a number: "))

# Calculating the sum
result = sum_of_numbers(num)

print("The sum of all numbers from 1 to", num, "is:", result)
