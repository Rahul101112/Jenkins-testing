# Simple Python Test Program

print("=== Welcome to Python Test Program ===")

# Function to greet user
def greet(name):
    print(f"\nHello, {name}! Welcome to Python.")

# Function to add numbers
def add_numbers(a, b):
    return a + b

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to print multiplication table
def multiplication_table(n):
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Take user input
name = input("Enter your name: ")
greet(name)

# Number operations
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))

    result = add_numbers(num1, num2)
    print(f"Sum: {result}")

    print(f"{num1} is {check_even_odd(num1)}")
    print(f"{num2} is {check_even_odd(num2)}")

    multiplication_table(num1)

except ValueError:
    print("Please enter valid numbers!")

# List operations
print("\n=== Working with Lists ===")
numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

numbers.append(6)
print("After adding 6:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)

print("Looping through list:")
for num in numbers:
    print(num)

# Dictionary example
print("\n=== Dictionary Example ===")
student = {
    "name": name,
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(f"{key}: {value}")

# Simple game
print("\n=== Guess the Number Game ===")
secret = 7

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct! 🎉")
else:
    print("Wrong guess 😢. The number was 7.")

print("\n=== Program Finished ===")
