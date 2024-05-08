class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right}, {self.height})"

class AVLTree:

    def __init__(self):
        self.root = None


    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))


    def insert(self, value):
        node = Node(value)
        if self.root is None:
            node.height = 0
            self.root = node
        else:
            self.root = self._insert_rec(self.root, node)
        return node


    def _insert_rec(self, root, node):
        if root is None:
            return node
       
        if node.value < root.value:
            root.left = self._insert_rec(root.left, node)
        elif node.value > root.value:
            root.right = self._insert_rec(root.right, node)

        root = self.fix_insert(root)
        return root

    def fix_insert(self, root):
        self.update_height(root)
        factor = self.get_factor(root)

        if factor > 1:
            if self.get_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        elif factor < -1:
            if self.get_factor(root.right) > 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def rotate_left(self, x):
        """Realizará a rotação esquerda utilizando como raiz o paramêtro `x`"""
        y = x.right
        tmp = y.left

        y.left = x
        
        x.right = tmp

        self.update_height(x)
        self.update_height(y)

        return y

    def rotate_right(self, x):
        y = x.left
        tmp = y.right

        y.right = x 
        x.left = tmp 
        self.update_height(x)
        self.update_height(y)

        return y


    def height(self, node):
        if node is None:
            return 0

        return node.height

    def get_factor(self, root):
        if root is None:
            return 0

        return self.height(root.left) - self.height(root.right)








