class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        return str(self.val)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.set_next(node2)
node2.set_next(node3)


# 遍历
cur_node = node1
while cur_node:
    print(cur_node)
    cur_node = cur_node.next

# 对应数据结构
# python stack
stack = [1, 2]
stack.append(3)
print(stack.pop())

# python 双向链表
from collections import deque
q = deque([2, 3])
q.appendleft(1)
q.append(4)
print(q)
q.popleft()
print(q)
q.pop()
print(q)