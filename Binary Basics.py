number = int(input("Enter a number:"))
guess = int(input("Guess the binary value of the number you entered:"))

print(f"\nYour Guess : {guess} | Actual Binary Value : {bin(number)[2:]}")

print()

first = int(input("Enter the first number for 'AND' Calculation:"))
second = int(input("Enter the second number for 'AND' Calculation:"))

print(f"\nThe result of {first} & {second} is : {first & second}")

print()

third = int(input("Enter the first value for 'OR' Calculation:"))
fourth = int(input("Enter the second value for 'OR' Calculation:"))

print(f"\nThe result of {third} | {fourth} is : {third | fourth}")