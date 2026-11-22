sub1 = int(input("Enter marks in Subject 1 (out of 100): "))
sub2 = int(input("Enter marks in Subject 2 (out of 100): "))
sub3 = int(input("Enter marks in Subject 3 (out of 100): "))

percentage = (sub1 + sub2 + sub3) / 300 * 100
print(f"Percentage: {percentage:.2f}%")

# Outer if: must score at least 40 in every subject to pass
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
    print("Result: Pass")

    # Inner if: assign grade
    if percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Result: Fail (less than 40 in at least one subject)")
    print("Grade: F")