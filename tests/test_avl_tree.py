import json
import pprint
import unittest
from src.avl_tree import AVLTree, Node

class TestAVLTree(unittest.TestCase):
    def test_avl_insert(self):
        tree = AVLTree()
        tree.insert(10)
        tree.insert(15)
        tree.insert(12)
        tree.delete(12)
        print(tree.find(15))

if __name__ == '__main__':
    unittest.main()
