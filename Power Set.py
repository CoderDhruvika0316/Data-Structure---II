print(f"-> Binary of Mask 5 : {bin(5)[2:]}\n-> Observation : Seclects postion 0 and 2.")

number = int(input("\nEnter a number:"))
guess = int(input(f"Guess how many subsets a set of {number} elements has:"))

print(f"\n-> Result : Subsets of {number} elements : {2 ** number}\n-> Your Guess : {guess}")