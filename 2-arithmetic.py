
# Taking three numbers from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Displaying the arithmetic operations
print("\n" + "=" * 45)
print("       ARITHMETIC OPERATIONS")
print("=" * 45)

# Performing basic arithmetic operations on a and b
print(f"Addition         : {a} + {b} = {a + b}")
print(f"Subtraction      : {a} - {b} = {a - b}")
print(f"Multiplication   : {a} * {b} = {a * b}")

# Checking if b is not zero before division
if b != 0:
    print(f"Division         : {a} / {b} = {a / b:.2f}")
    print(f"Floor Division   : {a} // {b} = {a // b}")
    print(f"Modulus          : {a} % {b} = {a % b}")
else:
    # Displaying a message if b is zero
    print("Division         : Not applicable (b is zero)")
    print("Floor Division   : Not applicable (b is zero)")
    print("Modulus          : Not applicable (b is zero)")

# Performing arithmetic operations using all three numbers
print("\n" + "=" * 45)
print("       OPERATIONS WITH THREE NUMBERS")
print("=" * 45)

print(f"Addition         : {a} + {b} + {c} = {a + b + c}")
print(f"Subtraction      : {a} - {b} - {c} = {a - b - c}")
print(f"Multiplication   : {a} * {b} * {c} = {a * b * c}")

# Checking if both divisors are not zero
if b != 0 and c != 0:
    print(f"Division         : {a} / {b} / {c} = {a / b / c:.2f}")
    print(f"Floor Division   : {a} // {b} // {c} = {a // b // c}")
    print(f"Modulus          : {a} % {b} % {c} = {a % b % c}")
else:
    # Displaying a message if any divisor is zero
    print("Division operations: Not applicable (zero divisor)")

# Evaluating expressions using operator precedence
print("\n" + "=" * 45)
print("       OPERATOR PRECEDENCE")
print("=" * 45)

# Calculating expressions with and without parentheses
result1 = a + b * c ** 2
result2 = (a + b) * c ** 2

# Displaying both expression results
print(f"a + b * c ** 2   = {result1}")
print(f"(a + b) * c ** 2 = {result2}")

# Calculating the difference between both results
print(f"Difference       = {result2 - result1}")

# Displaying the closing line
print("=" * 45)
