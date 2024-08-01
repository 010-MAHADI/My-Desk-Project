# Map Function
def squre(x):
    return x*x

num = [1,2,3,4,5]

valu = list(map(squre,num))
print(valu)



# Filter Function
num = [1,2,3,4,5,6]

calculation = list(filter(lambda x: x%2==0,num))
print(calculation)

