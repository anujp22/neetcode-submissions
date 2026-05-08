class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()
        for c in s:
            hashset.add(c)
        for c in t:
            if c not in hashset:
                return False
        return True