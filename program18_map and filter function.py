# Map Function
def squre(x):
    return x*x

num = [1,2,3,4,5]

valu = list(map(squre,num))
print(valu)

# Using Map Function

A, B, C, D = map(int, input("Enter values for A, B, C, D separated by spaces: ").split())

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")




# Filter Function
num = [1,2,3,4,5,6]

calculation = list(filter(lambda x: x%2==0,num))
print(calculation)

