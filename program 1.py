m = 80
if m >= 80:
    print("a+")
elif m >= 70:
    print("a")
elif m >= 60:
    print("a-")
elif m >= 50:
    print("b")
elif m >= 40:
    print("c")
else:
    print("Fail")
# 2nd method
if m >= 80 and m <= 100:
    print("a+")
if m >= 70 and m <= 79:
    print("a")
if m >= 60 and m <= 69:
    print("a-")
if m >= 50 and m <= 59:
    print("b")
if m >= 40 and m <= 49:
    print("c")
else:
    print("Fail")

#3rd method
if 80 <= m <=100:
    print("A+")
