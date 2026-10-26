first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
guess = int(input("Guess what the first number you have entered will become after using XOR Swap on your entered numbers:"))

print(f"Before :\n-> First Number : {first}\n-> Second Number -> {second}\n")

first ^= second
second ^= first
first ^= second

print(f"After :\n->First Number : {first}\n-> Second Number : {second}\nYour Guess for the first number : {guess}")