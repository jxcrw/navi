#!/usr/bin/env python3
"""Linked list sandbox"""

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Value = {self.value}; Next = {self.next.value}"

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return str([node.value for node in self])

    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            if location == 0: # Insert at beginning
                new_node.next = self.head
                self.head = new_node
            elif location == -1: # Insert at end
                self.tail.next = new_node
                self.tail = new_node
            else: # Insert in middle
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

                if temp_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            [print(node.value) for node in self]

    def reverse(self):
        head, prev = self.head, None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        self.tail = self.head
        self.head = prev

    def search_linear(self, target_value):
        if self.head is None:
            print("Linked list is empty.")
        else:
            for node in self:
                if node.value == target_value:
                    return node
            return "Specified value not found."

    def delete_node(self, location):
        if self.head is None:
            print("Linked list is empty.")
        else:
            if location == 0: # Delete at beginning
                if self.head == self.tail: # LL contains a single node
                    self.head = self.tail = None
                else: # LL contains multiple nodes
                    self.head = self.head.next
            elif location == -1: # Delete at end
                if self.head == self.tail: # LL contains a single node
                    self.head = self.tail = None
                else: # LL contains multiple nodes
                    for node in self:
                        if node.next == self.tail: break
                    node.next = None
                    self.tail = node
            else: # Delete in middle
                temp_node = self.head
                for i in range(location - 1):
                    temp_node = temp_node.next
                temp_node.next = temp_node.next.next

    def delete(self):
        self.head = self.tail = None


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert(1, -1)
    linked_list.insert(2, -1)
    linked_list.insert(3, -1)
    linked_list.insert(4, -1)

    linked_list.insert(0, 0)

    linked_list.insert(555, 3)

    print(linked_list)
    linked_list.traverse()

    print(linked_list.search_linear(555))
    print(linked_list.search_linear(999))

    linked_list.delete_node(0)
    print(linked_list)
    linked_list.delete_node(-1)
    print(linked_list)
    linked_list.delete_node(2)
    print(linked_list)

    linked_list.delete()
    print(linked_list)
    print()

    # ─────────────────────────────────────────────────────────────────────────────

    # Test out reverse() method (LeetCode 206)
    linked_list = SinglyLinkedList()
    for i in range(1, 6): linked_list.insert(i, -1)

    print(linked_list)
    print(linked_list.head)
    print(linked_list.tail.value, linked_list.tail.next)
    print()

    linked_list.reverse()
    print(linked_list)
    print(linked_list.head)
    print(linked_list.tail.value, linked_list.tail.next)
