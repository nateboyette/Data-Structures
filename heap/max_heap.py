class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(int(len(self.storage) - 1))

    def delete(self):

        root = self.storage[0]
        # last_index = len(self.storage) - 1
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        self.storage.pop()
        self._sift_down(0)

        return root

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # the index parameter is the index of the node wherever it is in the array

    def _bubble_up(self, index):
        # loop until either the element reaches the top of the array
        # or we'll break the loop when we realize the element's priority
        # is not larger than its parent's value
        while index > 0:
            # the value at 'index' fetches the index of its parent
            # has floor built in when using dbl slashes
            parent = (index-1) // 2
            # check if the element at 'index' has higher priority than
            # the elemetn at the parent index
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # we also need to update the index
                index = parent
            else:
                # otherwise, our element has reached a spot in the heap where its parent
                # element has higher priority; stop climbing
                break

    def _sift_down(self, index):

        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
        if left_child < len(self.storage) - 1 or right_child < len(self.storage) - 1:
            if self.storage[left_child] < self.storage[right_child]:
                if self.storage[index] < self.storage[right_child]:
                    self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
                    self._sift_down(right_child)
            else:
                if self.storage[index] < self.storage[left_child]:
                    self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
                    self._sift_down(left_child)
