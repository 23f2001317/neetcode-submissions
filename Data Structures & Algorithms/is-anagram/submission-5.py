class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)

        if (a == b) and (len(s) == len(t)):
            return True
        else:
            return False