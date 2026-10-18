input("XOR All Numbers - Pairs Cancel, The Odd One Stays. Press Enter to run:")

print("\n-> List : [1, 2, 3, 4, 3, 2, 1]")
print(f"-> Odd Ocurring : {1 ^ 2^ 3 ^ 4 ^ 3 ^ 2 ^ 1}\n")

number = int(input("Enter a number (try 7 or 11):"))

numbers = [3, number, 5, 3, 5]

guess = int(input(f"Guess which number in {numbers} appears once:"))

result = 0

for digit in numbers:
    result ^= digit

input("\n'XOR' Cancels Pairs - The Odd One Survives. Press Enter to run:")
print(f"\n-> List : {numbers}\n-> Odd Ocurring : {result}\n-> Your Guess : {guess}")