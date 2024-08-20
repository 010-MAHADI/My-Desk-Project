try:
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    sum = num1 / num2
    print(sum)

except ValueError:
    print("you have to insert only integer.")
except ZeroDivisionError:
    print("You can't divide a number by 0.")

finally:
    print("\nThank's for try !!!")



# 2nd part
def voter (age):
    if age < 18:
        raise ValueError("invalid voter")
    return "you are allowed to vote"

try:

    print(voter(43))

except ValueError:
    print("envalid")
