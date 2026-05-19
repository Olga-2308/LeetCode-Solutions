class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:

        seen = []
        ans = []
        k = 0

        # We check each number using a loop
        for num in nums:

            # If the number is greater than 0, then it is necessary to add it to the array of seen numbers
            if num > 0:
                seen.append(num)

                # and it is necessary to reset the counter -1, 
                # since the sequence of numbers -1 in the array is interrupted 
                # and the next values ​​need to be counted from the beginning
                k = 0

            # If we encounter -1, we increase the counter
            else:
                k += 1

                # The result must be added to the number from the array seen under the current index k. 
                # If k is less than the array length, then the number under index -k is added to the answer. 
                # Since the condition required adding values ​​to the beginning of the array, 
                # which would lead to a shift in the indices each time, during sequential addition, 
                # the elements are mirrored, and therefore, to find the desired element, 
                # you must search for it from the other side, and indices in the opposite direction have negative values.
                if k <= len(seen):
                    ans.append(seen[-k])

                # If k is greater than the length of the array, 
                # then the required value is physically not there and we write -1 in the result
                else:
                    ans.append(-1)

        return ans