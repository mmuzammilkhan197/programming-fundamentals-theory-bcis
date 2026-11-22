text = input("Enter a string: ")

# Positive and negative indexing
print("First character:", text[0])
print("Last character :", text[-1])

# Slicing
print("First five characters:", text[:5])
print("Reversed string:", text[::-1])

# Length
print("Total characters:", len(text))

# Membership check using the in operator
word = input("Enter a word to search: ")
if word in text:
    print(f"'{word}' exists in the string")
else:
    print(f"'{word}' does not exist in the string")