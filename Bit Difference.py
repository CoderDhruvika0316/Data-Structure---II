number = int(input("\nEnter a number:"))
digit = int(input("Enter another number:"))
guess = int(input(f"Guess how many digits differ between {number} and {digit}:"))

difference = bin(number ^ digit).count("1")
print(f"\n-> {number} ^ {digit} in Binary : {bin(number ^ digit)[2:]}\n-> Different Bits : {difference}\n->Your Guess : {guess}")