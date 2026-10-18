input("'XOR' - Keeps the Number. Press Enter to run:")

print(f"\n-> The result of 5 ^ 0 is : {5 ^ 0}")
print(f"-> The result of 9 ^ 0 is : {9 ^ 0}\n")

input("'XOR' with itself gives 0. Press Enter to run:")

print(f"\n-> The result of 5 ^ 5 is : {5 ^ 5}")
print(f"-> The result of 9 ^ 9 is : {9 ^ 9}\n")

number = int(input("Enter a number (try 6 or 11):"))
guess = int(input(f"Guess what the result of 3 ^ {number} ^ 3:"))

input("\n'XOR' Cancels - 3 appears twice so it disappears. Press Enter to run:")

print(f"\n-> The result of 3 ^ {number} ^ 3 is : {3 ^ number ^ 3}\n-> Your Guess was : {guess}")