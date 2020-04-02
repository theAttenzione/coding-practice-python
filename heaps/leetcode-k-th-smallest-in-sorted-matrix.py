# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(min(k, len(matrix))):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        count, smallest = 0, 0
        while heap:
            smallest, row, col = heapq.heappop(heap)
            count += 1
            if count == k:
                break
            if len(matrix) > col + 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return smallest