import json
import pprint
import unittest
from src.red_black_tree import RedBlackTree, Node, Color
from src.rbtree import RBTree

class TestRedBlackTreeMethods(unittest.TestCase):
    def test_left_rotation(self):
    #       10
    #   2      12 
    #             15
    #
      node4 = Node(Color.RED, value=15, left=None, right=None)
      node2 = Node(Color.RED, value=2, left=None, right=None)
      node3 = Node(Color.BLACK, value=12, left=None, right=node4)
      node1 = Node(color=Color.BLACK, parent=None, left=node2, right=node3, value=10)
      node4.parent = node3
      node3.parent = node1
      node2.parent = node1
      tree = RedBlackTree(root=node1)

      tree.rotate_left(node1)

      self.assertEqual(tree.root, node3)

    def test_insertion(self):
      node1 = Node(color=Color.BLACK, value=10)
      tree = RedBlackTree(root=node1)

      tree.insert(12)

      tree.insert(8)


      tree.insert(3)
      tree.insert(2)
      print(tree.root.left)

      tree.insert(1)

      # tree.insert(1)
      # tree.insert(11)
      #
      # tree.insert(13)
      #
      # self.assertEqual(tree.root.right.left.value, 11)
      # self.assertEqual(tree.root.right.left.color, Color.RED)
      #
      # self.assertEqual(tree.root.right.right.value, 15)
      # self.assertEqual(tree.root.right.right.value, Color.BLACk)
      #
      # self.assertEqual(tree.root.right.right.left.value, 13)
      # self.assertEqual(tree.root.right.right.left.value, Color.RED)
      #


if __name__ == '__main__':
    unittest.main()
