Str = input("Enter a string: ")

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
current_vowels = ""
output = []

for index, i in enumerate(Str):
    if i in vowels:
        current_vowels += i
    else:
        # Check if there's a valid group of vowels between consonants
        if len(current_vowels) > 1:
            if index > 0 and Str[index-1] in consonants and i in consonants:
                output.append(current_vowels)
        current_vowels = ""

# If there are any vowels left at the end and they are followed by a consonant
if len(current_vowels) > 1 and Str[-2] in consonants:
    output.append(current_vowels)

# Check if any valid groups of vowels were found
if output:
    for group in output:
        print(group)
else:
    print(-1)
