# r = readable
# w = writeable
# r+ = readable and writeable

file = open("testfile.txt","r")
# print(file.readable())

"""
# full text in one line as a list
text2 = file.readlines()[0]
print(text2)
"""

text = file.read()
print(text)

size = len(text)
print(size)

"""# by using for loop
for line in file:
    print(line)"""


file.close()


# writing in a file
# a = for add new text
file2 = open("testfile.txt","a")

file2.write("\nAm I ME")

file.close()