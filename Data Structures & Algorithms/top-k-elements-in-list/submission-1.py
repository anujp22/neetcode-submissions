class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        answer = [] 
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        for key, values in hashmap.items():
            bucket[values].append(key)
        for i in range(len(bucket)-1,-1,-1):
            for j in range(len(bucket[i])-1,-1,-1):
                if len(answer) < k:
                    answer.append(bucket[i][j])
                else:
                    break
            if len(answer) == k:
                break
        return answer
