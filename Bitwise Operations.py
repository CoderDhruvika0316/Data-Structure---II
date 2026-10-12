number = int(input("Enter a number:"))
guess = int(input(f"Left Shift doubles the value. Guess the value of {number} << 1:"))

print(f"The answer of {number} << 1 is : {number << 1}")

print(f"The answer of {number} >> 1 is : {number >> 1}")

first = int(input("Enter the first value for 'XOR' Calculation:"))
second = int(input("Enter the second value for 'XOR' Calculation:"))

print(f"The answer of {first} ^ {second} is : {first ^ second}")

print(f"The answer of 'NOT' Calculation is : {number & 0xFF}")