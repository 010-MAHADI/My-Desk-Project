import re

pattan = r"colour"
# match or search
if re.search(pattan," read is a colour , i love read colour"):
    print("match")
else:
    print("not match")

print(re.findall(pattan,"read is a colour , i love read colour"))



# 2 nd
pattan1 = r"colour"
text = "read is a colour"
match = re.search(pattan1,text)
if match :
    print(match.start())
    print(match.end())
    print(match.span())