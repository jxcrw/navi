#!/usr/bin/env python3
"""Tree sandbox"""

from __future__ import annotations


class Node:
    def __init__(self, data, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level=0):
        r = "  " * level + str(self.data) + "\n"
        for c in self.children:
            r += c.__str__(level + 1)
        return r

    def add_child(self, node: Node):
        self.children.append(node)


if __name__ == '__main__':
    tree = Node('Drinks', [])
    cold = Node('Cold', [])
    hot = Node('Hot', [])

    cola = Node('Cola', [])
    water = Node('Water', [])
    tea = Node('Tea', [])
    coffee = Node('Coffee', [])

    tree.add_child(cold)
    tree.add_child(hot)
    cold.add_child(water)
    cold.add_child(cola)
    hot.add_child(tea)
    hot.add_child(coffee)
    print(tree)
