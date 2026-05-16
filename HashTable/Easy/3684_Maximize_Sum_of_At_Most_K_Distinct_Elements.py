class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        # We convert a list into a set to remove duplicates from the list.
        num = set(nums)

        # we turn the set back into a list so that the elements of the list can be sorted in a strict, immutable order
        numbers = list(num)
        numbers.sort(reverse = True)

        # return k maximum values ​​of the list
        return numbers[:k]