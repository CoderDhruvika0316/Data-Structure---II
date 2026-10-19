input("[Number & Number - 1] - Clears Rightmost Set Bit. Press Enter to run:")

print(f"\n-> The Result of 12 & 11 is : {12 & 11}\n-> Binary of the Result : {bin(12 & 11)[2:]}")
print(f"\n-> The Result of 8 & 7 is : {8 & 7}")

number = int(input("\nEnter a number (try 4 or 6):"))
guess = input(f"Guess if {number} is a Power of 2 (YES/NO):")

input("\nPower of 2 :- [Number & Number - 1] == 0 - Only One Bit is ON. Press Enter to run:")

if number > 0 and (number & number - 1) == 0:
    print(f"\nResult :-\n-> {number} is a Power of 2. ✅\n-> Binary of the Result : {bin(number)[2:]}\n-> Your Guess : {guess}")

else:
    print(f"\nResult :-\n-> {number} is NOT a Power of 2. ❌\n-> Binary of the Result is : {bin(number)[2:]}\n-> Your Guess : {guess}")