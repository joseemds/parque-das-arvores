from dataclasses import dataclass
from enum import Enum
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Color(Enum):
    RED = 0
    BLACK = 1

    def __str__(self):
        if self == Color.RED:
            return "Red"
        elif self == Color.BLACK:
            return "Black"
# Example usage:

@dataclass
class Node(Generic[T]):
    color: Color
    value: T
    parent: Optional['Node[T]'] = None
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None

    def is_black(self):
        return self.color == Color.BLACK

    def is_red(self):
        return self.color == Color.RED


@dataclass
class RedBlackTree(Generic[T]):
    root: Node

    def rotate_left(self, x: Node[T]):
        """Realizará a rotação esquerda utilizando como raiz o paramêtro `x`"""
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: 
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x: Node[T]):
        """Realiza a rotação direita utilizando como raiz o paramêtro `x`"""
        y = x.left
        y.left = x.right

        if y.right != None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


    def fixup_insert(self, node: Node[T]):
        while node.parent.is_red():
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.is_red():
                    u.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        self.rotate_right(node.parent)
                node.parent.color = Color.BLACK
                node.parent.parent.color = Color.RED
                self.rotate_left(node.parent.parent)
            else:
                u = node.parent.parent.right
                if u and u.is_red():
                    u.color = Color.BLACK
                    u.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        self.rotate_left(node.parent)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rotate_right(node.parent.parent)

            if node == self.root:
                break
            
            self.root.color = Color.BLACK

    def _search_rec(self, node: Node[T], v:T):
        if not node or v == node.value:
            return node
        if v < node.value:
            return self._search_rec(node.left, v)

        return self._search_rec(node.right, v)


    def search(self, v: T): 
        return _search_rec(self.root, v)


    # def _delete_rec(self, node: Node[T], v):
    #     curr = None
    #     while node is not None:
    #         if node.value == v:
    #             curr = v
    #
    #         if node.value < key:
    #             node = node.right
    #         else:
    #             node = node.left
    #
    #
    #     if curr is None:
    #         print("Nao foi encontrado valor: " + v)
    #
    #     tmp = curr
    #     tmp_color = tmp.color
    #
    #     if curr.left is None:
    #         x = curr.right
            

    def delete(self, v: T):
        self._delete_rec(self.root, v)




    def insert(self, v: T):
        node = Node(value=v, color=Color.RED)

        curr = None
        looking_at = self.root

        while looking_at is not None:
            curr = looking_at
            if v < curr.value:
                looking_at = curr.left
            else:
                looking_at = curr.right

        node.parent = curr

        if curr == None:
            self.root = node
        elif v < curr.value:
            curr.left = node
        elif v > curr.value:
            curr.right = node


        if node.parent is None:
          self.root.color = Color.BLACK
          return

        if node.parent.parent is None:
          return
        
        self.fixup_insert(node)

    def delete(self, node: Node[T]):

