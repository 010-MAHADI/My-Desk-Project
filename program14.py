# stack
books = []
books.append("Learn c")
books.append("Learn c++")
books.append("Learn java")
print(books)

books.pop()
print("the top book is ",books[-1])

books.pop()
print("the top book is ",books[-1])

books.pop()
if not books:
    print("no Books av")