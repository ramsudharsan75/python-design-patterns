from bisect import bisect_right
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mem = defaultdict(list)

        for i, ch in enumerate(s):
            mem[ch].append(i)

        prev = None
        res = {}

        for ch in sorted(set(s)):
            if prev is None:
                res[ch] = mem[ch][0]
            else:
                x = min(len(mem[ch]) - 1, bisect_right(mem[ch], prev))
                res[ch] = mem[ch][x]

            prev = res[ch]

        return "".join(list(sorted(res.keys(), key=lambda ch: res[ch])))


s = Solution()
s.removeDuplicateLetters("bcabc")
