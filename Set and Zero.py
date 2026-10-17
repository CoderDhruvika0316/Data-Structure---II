input("Setting a Bit - 'OR' turns it ON. Press Enter to run:")

print(f"\n5 in Binary : {bin(5)[2:]}")
print(f"The value of 5 | 2 is : {5 | 2}\nThe Binary Value of the result is : {bin(5 | 2)[2:]}")

input("\nZeroing a Bit - The 'AND' Bitwise Operator turns a bit OFF. Press Enter to run:")

print(f"\nBinary of 7 is : {bin(7)[2:]}")
print(f"The value of 7 & 5 is : {7 & 5}\nThe Binary Value of the result is : {bin(7 & 5)[2:]}")

number = int(input("\nEnter a number (try using 4 or 6):"))
guess = input("Guess if the number you have entered is a power of 2: (YES/NO)")

if number > 0 and (number & (number - 1)) == 0:
    print(f"\n{number} in Binary : {bin(number)[2:]}\n{number} is a power of 2. Your guess was : '{guess}'")

else:
    print(f"\n{number} in Binary : {bin(number)[2:]}\n{number} is not a power of 2. Your guess was : '{guess}'")