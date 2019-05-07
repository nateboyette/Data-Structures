"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def get_value(self):
        return self.value

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

    def remove_from_head(self):
        if self.head == self.tail:
            deleted_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return deleted_value
        else:
            deleted_value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return deleted_value

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.tail.next = None
            self.length += 1

    def remove_from_tail(self):
        new_tail = self.tail.prev
        old_tail = self.tail
        self.tail.delete()
        self.tail = new_tail
        self.length -= 1
        return old_tail.value

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        self.add_to_tail(node.value)

    def delete(self, node):
        if node.prev is None:
            node.remove_from_head()
        elif node.next is None:
            node.remove_from_tail()
        else:
            self.length -= 1
            node.delete()

    def get_max(self):
        pass


dblList = DoublyLinkedList()

dblList.add_to_head(2)
dblList.add_to_head(55)
dblList.add_to_head(60)
dblList.add_to_tail(20)
dblList.add_to_tail(30)
dblList.remove_from_head()
dblList.remove_from_tail()

print(dblList.head.next.get_value())
print(dblList.head.get_value())
print(dblList.tail.get_value())
