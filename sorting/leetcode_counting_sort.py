# https://leetcode.com/problems/sort-an-array/

from collections import Counter

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum, minimum = max(nums), min(nums)
        counter = Counter(nums)
        sorted_array = []
        for i in range(minimum, maximum+1):
            if i in counter:
                sorted_array += [i] * counter[i]
        return sorted_array