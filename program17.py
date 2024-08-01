
# xarge
def add(*number):
    sum = 0
    for y in number:
        sum = sum + y
    return sum

print(add(10,20,30))
print(add(154,4,14,234,43))
print(add(24,3443,43,4))


# xxarge
def student(**details):
    print(details["id"])

student(id = 133,name= "mahadi")