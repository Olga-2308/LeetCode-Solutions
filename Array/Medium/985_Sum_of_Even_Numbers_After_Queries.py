class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        result = []
        total = 0

        # we find the total sum of all even numbers in the array
        for num in nums:
            if num % 2 == 0:
                total += num

        # We process each request in turn
        for i in range(len(queries)):

            # we determine the number that needs to be processed
            indx = queries[i][1]

            # we determine the number that needs to be added
            adding = queries[i][0]

            # We need to check if the number is even and whether it was added to the total. 
            # If the number is even, we subtract it from the total.
            if nums[indx] % 2 == 0:
                total -= nums[indx]

            # we change the number according to the request
            nums[indx] += adding

            # If the resulting number is even, then we add it to the total sum
            if nums[indx] % 2 == 0:
                total += nums[indx]

            result.append(total)

        return result