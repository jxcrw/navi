#!/usr/bin/env python3
"""Queue sandbox"""
from typing import Any


class QueueCircular:
    """Fixed-capacity queue backed by vanilla Python List."""

    _MESSAGE_EMPTY = "Queue is empty."
    _MESSAGE_FULL = "Queue is full."

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(i) for i in self.items]
        return ' '.join(values)

    def is_full(self) -> bool:
        is_top_nextto_start = self.top + 1 == self.start
        is_first_last = self.start == 0 and self.top + 1 == self.capacity
        return True if is_top_nextto_start or is_first_last else False

    def is_empty(self) -> bool:
        return True if self.top == -1 else False

    def enqueue(self, val):
        if self.is_full(): print(self._MESSAGE_FULL)
        else:
            if self.top + 1 == self.capacity:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = val

    def dequeue(self) -> Any:
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.capacity:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self) -> Any:
        if self.is_empty(): print(self._MESSAGE_EMPTY)
        else:
            return self.items[self.start]

    def delete(self):
        self.items = [None] * self.capacity
        self.top = -1
        self.start = -1



if __name__ == '__main__':
    queue = QueueCircular(2)
    queue.enqueue(0)
    queue.enqueue(1)
    print(queue.dequeue())
    print(queue)
    print(queue.is_full())
