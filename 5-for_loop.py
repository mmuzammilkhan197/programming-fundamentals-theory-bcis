n = int(input("Enter a positive integer N: "))

# Even numbers from 1 to N
print("Even numbers:", end=" ")
for i in range(2, n + 1, 2):
    print(i, end=" ")

# Sum of odd numbers
odd_sum = 0
for i in range(1, n + 1, 2):
    odd_sum += i

# Factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("\nSum of odd numbers:", odd_sum)
print("Factorial:", factorial)