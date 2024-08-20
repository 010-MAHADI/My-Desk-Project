import re
partan = r"colour"
text = "my favourite colour is red. i love blue colour also"
text2 = re.sub(partan,"color",text) # count=2 replace number
print(text2)