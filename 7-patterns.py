# Pattern A: stars
print("Pattern A")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Pattern B: numbers
print("\nPattern B")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()