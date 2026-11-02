class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

       
        def run_piles(k):
            count = 0
            for i in range(len(piles)):
                count += (piles[i] + k - 1) // k
            return count 
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if run_piles(mid) <= h:
                right = mid 
            else:
                left = mid + 1
        
        return right