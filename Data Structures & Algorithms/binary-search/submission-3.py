class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index_list = list(enumerate(nums))

        for i in range(len(index_list)):
            if target == index_list[i][1]:
                return index_list[i][0]       
        return -1