# Python Display-Only Test Program

print("=== Python Test Program (No Input) ===\n")

# Function to greet
def greet():
    print("Hello! Welcome to Python testing.\n")

# Function to show numbers
def show_numbers():
    print("Numbers from 1 to 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")

# Function to check even/odd
def even_odd_demo():
    print("Even or Odd Check:")
    for i in range(1, 6):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
    print()

# Function to show multiplication tables
def tables():
    print("Multiplication Tables (1 to 3):")
    for i in range(1, 4):
        print(f"\nTable of {i}:")
        for j in range(1, 6):
            print(f"{i} x {j} = {i*j}")
    print()

# List demo
def list_demo():
    print("List Demo:")
    fruits = ["Apple", "Banana", "Mango"]
    print("Original list:", fruits)

    fruits.append("Orange")
    print("After adding Orange:", fruits)

    print("Looping through list:")
    for fruit in fruits:
        print(fruit)
    print()

# Dictionary demo
def dict_demo():
    print("Dictionary Demo:")
    student = {
        "name": "John",
        "age": 21,
        "course": "Python"
    }

    for key, value in student.items():
        print(f"{key}: {value}")
    print()

# Pattern printing
def pattern():
    print("Star Pattern:")
    for i in range(1, 6):
        print("*" * i)
    print()

# Main program
greet()
show_numbers()
even_odd_demo()
tables()
list_demo()
dict_demo()
pattern()

print("=== Program Finished Successfully ===")
