# https://leetcode.com/problems/minimum-path-sum/

class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = [[-1] * len(grid[0]) for _ in range(len(grid))]
        return self._min_path_sum(len(grid) - 1, len(grid[0]) - 1, grid, cache)

    def _min_path_sum(self, i, j, grid, cache):
        paths_to = self._paths_to(i, j)
        if not paths_to:
            return grid[i][j]

        paths_to_cost = []
        for pi, pj in paths_to:
            if cache[pi][pj] == -1:
                cache[pi][pj] = self._min_path_sum(pi, pj, grid, cache)
            paths_to_cost.append(cache[pi][pj])

        return grid[i][j] + min(paths_to_cost)

    def _paths_to(self, i, j):
        if i == 0 and j:
            return [(0, j - 1)]
        if j == 0 and i:
            return [(i - 1, 0)]
        if j and i:
            return [(i - 1, j), (i, j - 1)]
        return []