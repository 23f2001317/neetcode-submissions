from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums)

        for key, value in num.items():
            if value >= 2:
                return True
            
        return False