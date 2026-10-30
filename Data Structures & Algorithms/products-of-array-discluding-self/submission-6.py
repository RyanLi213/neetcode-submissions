class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_prefix = [1]
        reverse_nums = nums[::-1]
        rev_prefix = [1]
        for x in nums:
            forward_prefix.append(forward_prefix[-1]*x) 
        for y in reverse_nums:
            rev_prefix.append(rev_prefix[-1]*y)
        forward_prefix.pop()
        rev_prefix.pop()
        prod = []
        for i in range(len(nums)):
            prod.append(forward_prefix[i]*rev_prefix[-(i+1)])
        return prod