# Take student details
name = input("Enter student's name: ")
reg_no = input("Enter registration number: ")
age = int(input("Enter age: "))

sub1 = int(input("Enter marks in Subject 1 (out of 100): "))
sub2 = int(input("Enter marks in Subject 2 (out of 100): "))
sub3 = int(input("Enter marks in Subject 3 (out of 100): "))

# Calculations
total = sub1 + sub2 + sub3
average = total / 3
percentage = (total / 300) * 100

# Display report
print("\n" + "=" * 40)
print("        STUDENT REPORT CARD")
print("=" * 40)
print(f"Name                : {name}")
print(f"Registration No.    : {reg_no}")
print(f"Age                 : {age} years")
print("-" * 40)
print(f"Total Marks         : {total} / 300")
print(f"Average Marks       : {average:.2f}")
print(f"Percentage          : {percentage:.2f}%")
print("=" * 40)