class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSorted = sorted(s)
        tSorted = sorted(t)
        i = 0
        while i < len(s):
            if sSorted[i]!=tSorted[i]:
                return False
            i+=1
        return True