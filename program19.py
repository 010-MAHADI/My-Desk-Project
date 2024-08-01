# List Comprehensions
ha = [1,2,3,4,5,6]

val = [x*x for x in ha]
print(val)


# 2nd methord
num = [1,2,3,4,5,6]
result = [x for x in num if x % 2 ==0]
print(result)