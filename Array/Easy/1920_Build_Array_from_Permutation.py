class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_lst = []
        for i in range(len(nums)):
            num = nums[nums[i]]
            new_lst.append(num)

        return(new_lst)