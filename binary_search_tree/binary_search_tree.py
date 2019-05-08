class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        # check if the new node's value is less than the current node's value
        if value < self.value:
            # check if there is no left child
            if not self.left:
                # park the new_node here
                self.left = BinarySearchTree(value)
            else:
                # Otherwise, we have to keep traversing further down since there exists
                # a left child
                self.left.insert(value)

          # do the same on the right side if the node's value >= the current node's value
        else:
                # check if theere is no right childe
            if not self.right:
                # park the value here
                self.right = BinarySearchTree(value)
            else:
                # keep recursing down to the right since there is a right child
                self.right.insert(value)

    def contains(self, target):
        current_node = self

        while current_node is not None:
            if target == current_node.value:
                return True
            elif current_node.left is None and current_node.right is None:
                break
            elif target < current_node.value:
                current_node = current_node.left
                print(current_node)
                current_node.contains(target)
            elif target > current_node.value:
                current_node = current_node.right
                print(current_node)
                current_node.contains(target)
        return False

    def get_max(self):

        max_value = self.value
        current_node = self
        while current_node:
            if current_node.left is None and current_node.right is None:
                break
            elif current_node.right.value > max_value:
                max_value = current_node.right.value
                current_node = current_node.right
                return current_node.get_max()
            else:
                current_node = current_node.right
                return current_node.get_max()

        return max_value

    def for_each(self, cb):

        current_node = self
        left_node = self.left
        right_node = self.right
        cb(self.value)
        if left_node is None and right_node is None:
            return
        elif left_node and right_node:
            left_node.for_each(cb)
            right_node.for_each(cb)
        elif left_node is not None and right_node is None:
            left_node.for_each(cb)
        elif right_node is not None and left_node is None:
            right_node.for_each(cb)
