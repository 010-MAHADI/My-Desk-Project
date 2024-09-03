from collections import deque

bank =deque(["Radoy", "ismail", "jahaid"])
bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

if not bank:
    print("no man availlavle")