class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):

        if not self.head and not self.tail:
            return None

        if self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None

            return old_head.get_value()
        else:
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def contain(self, value):
        if not self.head and not self.tail:
            return None

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
