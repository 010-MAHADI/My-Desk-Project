import re
partan = r"colo..ur" # ^and$ mining must
if re.match(partan,"coloyrur"):
    print("Match")



partan1 = r"a+" # a+ = 1 or more ,a* = 0 or more
if re.match(partan1,"acaoloyrur"):
    print("Matched2")



partan2 = r"ice(-)?cream"
if re.match(partan2,"icecream"):
    print("Matched3")


partan1 = r"ice(-)?cream"
if re.match(partan2,"icecream"):
    print("Matched3")
