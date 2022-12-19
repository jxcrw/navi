#!/usr/bin/env python3
"""Stack sandbox"""

from typing import Any

from linked_list.singly_linked_list import Node, SinglyLinkedList


class Stack:
    """Stack backed by vanilla Python list."""
    _MESSAGE_EMPTY = "Stack is empty."

    def __init__(self):
        self._list = []

    def __str__(self):
        vals = [str(x) for x in reversed(self._list)]
        return ', '.join(vals)

    def is_empty(self) -> bool:
        return False if self._list else True

    def push(self, val: Any):
        self._list.append(val)

    def pop(self):
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            return self._list.pop()

    def peek(self):
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            return self._list[-1]

    def delete(self):
        self._list = None


class StackLL:
    """Stack backed by singly linked list."""
    _MESSAGE_EMPTY = "Stack is empty."

    def __init__(self):
        self._linked_list = SinglyLinkedList()

    def __str__(self):
        vals = [str(x.value) for x in self._linked_list]
        return ', '.join(vals)

    def is_empty(self) -> bool:
        return False if self._linked_list.head else True

    def push(self, val: Any):
        node = Node(val)
        node.next = self._linked_list.head
        self._linked_list.head = node

    def pop(self):
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            node_val = self._linked_list.head.value
            self._linked_list.head = self._linked_list.head.next
            return node_val

    def peek(self):
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            node_val = self._linked_list.head.value
            return node_val

    def delete(self):
        self._linked_list.head = None


if __name__ == '__main__':
    # Vanilla Python list stack
    stack = Stack()
    print(stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)

    popped = stack.pop()
    print(popped)
    print(stack)

    peeked = stack.peek()
    print(peeked)

    # Linked list stack
    stack_ll = StackLL()
    print(stack_ll.is_empty())

    stack_ll.push(1)
    stack_ll.push(2)
    stack_ll.push(3)
    print(stack_ll)

    popped = stack_ll.pop()
    print(popped)
    print(stack_ll)

    peeked = stack_ll.peek()
    print(peeked)

