class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset = set()
        for c in s:
            hashset.add(c)
        for c in t:
            if c not in hashset:
                return False
        return True