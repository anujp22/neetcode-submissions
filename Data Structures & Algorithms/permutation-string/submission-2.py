class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        # for i in range(len(s2)-len(s1)+1):
        #     window = s2[i:i+len(s1)]
        #     temp = Counter(window)
        #     if temp == s1count:
        #         return True
        # return False

        l = 0
        r = len(s1) - 1
        window = deque()
        for i in range(r+1):
            window.append(s2[i])
        while r < len(s2):
            if Counter(window) == s1count:
                return True
            else:
                window.append(s2[r])
                window.popleft()
                l += 1
                r += 1
        return False
