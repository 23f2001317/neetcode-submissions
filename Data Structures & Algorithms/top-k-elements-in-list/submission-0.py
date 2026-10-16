from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        num = sorted(num, key=num.get, reverse=True)
        return num[:k]
