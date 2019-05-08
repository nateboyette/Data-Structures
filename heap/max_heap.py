class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    # the index parameter is the index of the node wherever it is in the array
    def _bubble_up(self, index):
        # loop until either the element reaches the top fo the array
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
        pass
