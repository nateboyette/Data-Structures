from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        return self.storage.tail.get_value()

    def dequeue(self):
        return f"{self.storage.head.get_value()} was removed"
        self.storage.remove_head()

    def len(self):
        self.size = 0
        if not self.storage.head and not self.storage.tail:
            return 0

        if self.storage.head == self.storage.tail:
            return 1

        current_value = self.storage.head

        while current_value:
            self.size += 1
            current_value = current_value.get_next()

        return self.size


q = Queue()

print(q.len())
q.enqueue(2)
print(q.len())
q.enqueue(4)
print(q.len())
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.enqueue(12)
q.enqueue(14)
q.enqueue(16)
q.enqueue(18)
print(q.len())
