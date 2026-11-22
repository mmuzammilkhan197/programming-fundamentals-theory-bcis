sentence = input("Enter a sentence: ")

# Uppercase and lowercase
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# Count vowels using a loop
vowels = 0
for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
print("Number of vowels:", vowels)

# Count spaces
print("Number of spaces:", sentence.count(" "))

# Replace a word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After replacing:", sentence.replace(old, new))

# Palindrome check (ignore spaces and case)
cleaned = sentence.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("The sentence is a palindrome")
else:
    print("The sentence is not a palindrome")