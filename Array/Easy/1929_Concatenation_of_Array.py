class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # fold the line 2 times from its beginning to the end
        result = nums[::] + nums[::]
        return result