class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)

        if self.end is not None:
            self.end.next = node

        self.end = node

        if self.start is None:
            self.start = self.end

        self.size += 1

    def dequeue(self):
        if self.start is None:
            return None

        node = self.start
        self.start = self.start.next

        if self.start is None:
            self.end = None

        self.size -= 1
        return node.value

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.start = None
        self.end = None
        self.size = 0

    def peek(self):
        if self.start is None:
            return None

        return self.start.value

    def print(self):
        node = self.start
        while node:
            print(node.value)
            node = node.next

    def to_array(self):
        array = []
        node = self.start
        while node:
            array.append(node.value)
            node = node.next

        return array
