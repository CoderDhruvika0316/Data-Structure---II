input("Power of 4 : [Number % 3 == 1]\nPower of 8 : [Number % 7 == 1].\nPress Enter to run:")

print(f"\n-> Binary of 16 : {bin(16)[2:]}\n-> The Result of 16 % 3 is : {16 % 3}\n-> Is 16 a Power of 4 : YES ✅")
print(f"\n-> Binary of 8 : {bin(8)[2:]}\n-> The Result of 8 % 7 is : {8 % 7}\n-> Is 8 a Power of 8 : YES ✅")

number = int(input("\nEnter a number (try 64 or 32):"))
guess = input(f"Guess if {number} is a Power of 4 (YES/NO):")

input(f"\nCheck [Number % 3 == 1]. Press Enter to Run.")

powering_through_fours = number > 0 and (number & (number - 1)) == 0 and number % 3 == 1

if powering_through_fours:
    print(f"- Result :-\n{number} is a Power of 4. ✅\n-> Binary of the Number : {bin(number)[2:]}\n-> Your Guess : {guess}")

else:
    print(f"- Result :-\n-> {number} is NOT a Power of 4. ❌\n-> Binary of the Number : {bin(number)[2:]}\n-> Your Guess : {guess}")