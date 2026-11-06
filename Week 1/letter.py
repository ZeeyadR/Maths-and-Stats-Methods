import random
letters = "abcdefghijklmnopqrstuvwxyz"
input_letter = random.choice(letters)

# don't edit the code above
# put your code below here:

print(input_letter)

output = "None"

if input_letter == "a" or input_letter == "e" or input_letter == "i" or input_letter == "o" or input_letter == "u":
    output = "Vowel"
elif input_letter == "y":
    output = "It depends"
else:
    output = "Consonant"
print("\n"+output)
