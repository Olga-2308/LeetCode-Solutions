class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        odd = []
        even = []

        # sort numbers from an array into new lists of even and odd numbers
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        result = []

        # We create the final list by adding numbers to the list one by one—even numbers to even-indexed positions, 
        # and odd numbers to odd-indexed positions. 
        # Since the length of the given array is even, and the number of even and odd numbers is the same, 
        # no additional checks or conditions are required.
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])

        return result