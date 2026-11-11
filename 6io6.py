def is_power4(n):
    if n <= 0:
        return False
    if n== 1:
        return True
    if n % 4 == 0:
        return is_power4(n // 4)
    return False

n = int(input("Enter a number: "))
guess = int(input(f"What is the power of {n}?: "))
print(f"is power of 4 {n} : {is_power4(n)}, your guess: {guess}")

if guess == is_power4(n):
    print("Correct")
else:
    print("Wrong")