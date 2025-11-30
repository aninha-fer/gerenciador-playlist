class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None

        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def peek(self):
        if self.top is None:
            return None

        return self.top.value

    def print(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def to_array(self):
        array = []
        current_node = self.top
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next

        return array

    def is_empty(self):
        return self.size == 0