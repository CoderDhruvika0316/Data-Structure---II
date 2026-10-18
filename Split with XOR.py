input("'XOR' All - Pairs Cancel, Two Occurring Ones Remain. Press Enter to run:")

xor_of_all = 1 ^ 4 ^ 3 ^ 3 ^ 5 ^ 5
print(f"\n-> List : [1, 4, 3, 3, 5, 5]\n-> XOR of All : {xor_of_all}\n-> Binary : {bin(xor_of_all)[2:]}\n")

print("-> Split Bit 1 :-\n- Group A (Bit 0 [ON]) : 1\n- Group B (Bit 0 [OFF]) : 4\n")

number = int(input("Enter a number (try 6 or 9):"))
guess = input(f"Guess if the Bit 0 of {number} is ON (YES/NO):")

input("\nCheck the Split Bit. press Enter to run:")

if number & 1:
    print(f"\n{number} :-\n-> Binary : {bin(number)[2:]}\n-> Bit 0 [ON] - Group A\n-> Your Guess : {guess}")

else:
    print(f"{number} :-\n-> Binary : {bin(number)[2:]}\n-> Bit 0 [OFF] - Group B\n-> Your Guess : {guess}")