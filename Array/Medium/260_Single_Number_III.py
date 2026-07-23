class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        With the help of a set, we can easily determine whether a number is a duplicate or not. 
        If the number is in the set, and in the iteration of the cycle we found the second one that is the same, 
        then it is a duplicate
        '''

        result = set()

        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)

        return list(result)