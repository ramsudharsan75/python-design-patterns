from bisect import bisect_right
from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        mat = defaultdict(list)
        indegrees = [0] * n
        roots = set(i for i in range(n))

        for pre, post in relations:
            mat[pre - 1].append(post - 1)
            indegrees[post - 1] += 1

            if indegrees[post - 1] > 0:
                roots.discard(post - 1)

        res = 0
        q = deque()

        for root in roots:
            period = time[root]
            res = max(res, period)
            q.append((root, period))

        print(q)
        mem = defaultdict(int)

        while q:
            course, period = q.popleft()

            for child in mat[course]:
                if mem[child] >= period + time[course]:
                    continue

                mem[child] = period + time[course]
                res = max(res, mem[child])
                q.append((child, mem[child]))

        return res


s = Solution()
s.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5])
