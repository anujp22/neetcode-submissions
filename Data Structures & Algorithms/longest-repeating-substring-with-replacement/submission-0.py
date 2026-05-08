class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_freq = 0
        max_length = 0
        l = 0
        r = 0
        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            max_freq = max(max_freq, hashmap[s[r]])
            if r-l+1 - max_freq <= k:
                max_length = max(max_length,(r-l+1))
            else:
                hashmap[s[l]]-= 1
                l += 1
            r+=1
        return max_length