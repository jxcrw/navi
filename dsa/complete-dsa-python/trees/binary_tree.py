#!/usr/bin/env python3
"""Binary tree sandbox"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self, level=0):
        return str(self.data)

    def __repr__(self, level=0):
        return str(self.data)


def preorder_traverse(node: Node):
    if not node: return
    print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node: Node):
    if not node: return
    inorder_traverse(node.left)
    print(node.data)
    inorder_traverse(node.right)

def postorder_traverse(node: Node):
    if not node: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data)

def levelorder_traverse(node: Node):
    if not node: return
    q = deque([node])
    while q:
        node = q.popleft()
        print(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)


if __name__ == '__main__':
    root = Node('Drinks')
    cold = Node('Cold')
    hot = Node('Hot')

    cola = Node('Cola')
    water = Node('Water')
    tea = Node('Tea')
    coffee = Node('Coffee')

    root.left = cold
    root.right = hot

    cold.left = water
    cold.right = cola
    hot.left = tea
    hot.right = coffee

    preorder_traverse(root)
    print()
    inorder_traverse(root)
    print()
    postorder_traverse(root)
    print()
    levelorder_traverse(root)
