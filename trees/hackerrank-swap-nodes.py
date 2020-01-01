#!/bin/python3

import os
import sys
from collections import deque

sys.setrecursionlimit(1024 + 4)


#  https://www.hackerrank.com/challenges/swap-nodes-algo/problem


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, indexes):
        self.root = Node(1)
        queue = deque()
        queue.append(self.root)
        for child_indexes in indexes:
            node = queue.popleft()
            left_index, right_index = child_indexes
            if left_index != -1:
                node.left = Node(left_index)
                queue.append(node.left)
            if right_index != -1:
                node.right = Node(right_index)
                queue.append(node.right)


def swap_nodes(indexes, queries):
    traversed = []
    tree = Tree(indexes)
    for required_depth in queries:
        _swap_at_depth(tree.root, required_depth)
        traversed.append(_traverse(tree.root))
    return traversed


def _swap_at_depth(node, required_depth, current_depth=1):
        if current_depth % required_depth == 0:
            node.left, node.right = node.right, node.left
        if node.left:
            _swap_at_depth(node.left, required_depth, current_depth + 1)
        if node.right:
            _swap_at_depth(node.right, required_depth, current_depth + 1)


def _traverse(node):
    return [
        *(_traverse(node.left) if node.left else []),
        node.value,
        *(_traverse(node.right) if node.right else [])
    ]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = swap_nodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()
