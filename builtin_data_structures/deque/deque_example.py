from collections import deque

dq = deque()

# Add item to deque
dq.append("A")
dq.append("B")
dq.appendleft("C")
dq.appendleft("D")

# Removing item from the right side
right = dq.pop()
print(right)

# Removing item from the left side
left = dq.popleft()
print(left)

if not dq:
    print("empty")

