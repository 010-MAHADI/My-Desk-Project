
num = [10, 20, 30, 40]
print(num)


for x in num:
    print(x)

# if i use while loop fo same work
index = 0
n = len(num)
while index < n:
    print(num[index])
    index = index + 1


# Series
# 1 + 2 + 3 + 4 + .......+n
N = int(input("enter the number: "))

sum = 0
for x in range(1,N+1):
    sum = sum + x
print(sum)


#
N1 = int(input("enter the number: "))

sum1 = 0
for x in range(1,N1+1,1):
    sum1 = sum1 + x*x
print(sum1)