number = int(input("\nEnter a number:"))
digit = int(input("Enter another number:"))

guess = int(input(f"\nGuess what is Bit {digit} of {number} (0/1):"))

print(f"\n-> Bit 2 of {number} : {(number >> digit) & 1}\n-> Your Guess : {guess}")