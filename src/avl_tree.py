class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        
        if self.root = None:
            self.root = none
            return

        if key < root.value:
            return

    def _insert_rec(self, root, value):
        if value < root.left:
            root.left = self._insert_rec(root.left, key)
        elif value > root.right:
            root.right = self._insert_rec(root.right, key)

        root.height = max(root.left.height, root.right.height)

        factor = get_factor(root)

        if factor > 1:
            if value < root.left.value:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        elif factor < -1:
            if value > root.right.value:
                return self.rotate_left(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)


        return root


    def rotate_left(...):
        pass

    def rotate_right(...):
        pass

    def get_factor(self, root):
        if root is None:
            return 0
        return root.left.height - root.right.height








