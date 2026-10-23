class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)

        for i in range(len(nums)):
            counter[nums[i]] +=1
        
        ordered = sorted(list(counter.items()), key = lambda x: x[1], reverse= True)
        
        list_max = []
        for j in range(k):
            list_max.append(ordered[j][0])
        
        return list_max