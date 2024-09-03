# stack, Last in first out
books = []
books.append("Learn c")
books.append("Learn c++")
books.append("Learn java")
print(books)

books.pop()
print("the top book is ",books[-1])

books.pop()
print(books)
print("the top book is ",books[-1])

books.pop()
if not books:
    print("no Books av")
    

# Queue, It's like a bank. First in first out 
from collections import deque

bank = deque([ "x", "y', "z"])
bank.popleft()
print(bank)
