# Example 6: using list as stacks and queues

# Stack operations (Last In, First Out - LIFO)

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("Popped item from stack:", popped_item)  # Output: Popped item from stack: 3

# Queue operations (First In, First Out - FIFO)
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft()
print("Dequeued item from queue:", dequeued_item)  # Output: Dequeued item from queue: 1
