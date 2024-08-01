
numberofword = 1
numberofletter = 0
numberofdigits = 0
usr = input("Enter The Word: ")
for x in usr:
    x = x.lower()
    if x >= "a" and x <= "z":
        numberofletter = numberofletter + 1
    elif x >= "0" and x <= "9":
        numberofdigits = numberofdigits + 1
    elif x == " ":
        numberofword = numberofword + 1

print("numberofword", numberofword)
print("numberofdigits", numberofdigits)
print("numberofletter", numberofletter)
"""

numberofword = 0
numberofletter = 0
numberofdigits = 0

usr = input("Enter the Sentence: ")

for x in usr:
    x = x.lower()
    if x >= "a" and x <= "z":
        numberofletter += 1
    elif x >= "0" and x <= "9":
        numberofdigits += 1
    elif x == " ":
        numberofword += 1

# Count the last word if the sentence doesn't end with a space
if usr[-1] != ' ':
    numberofword += 1

print("Number of words:", numberofword)
print("Number of digits:", numberofdigits)
print("Number of letters:", numberofletter)
"""