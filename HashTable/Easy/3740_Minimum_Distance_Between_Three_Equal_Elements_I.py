class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        freq = {}

        # we determine the frequency of each element in the array
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        t = []

        # If a number appears less than 3 times in the array, 
        # it doesn't suit us and we skip it.
        for i in range(len(nums)):
            if freq[nums[i]] < 3:
                continue

            # and if the number occurs 3 or more times, 
            # then we write each pair as: the number and its index in the array
            else:
                t.append([nums[i], i])

        # We sort the resulting array so that identical numbers are together (not indexes), 
        # since sorting is by the first element of the subarray
        t.sort()
        minimum_distance = []

        # If the array length is 0, this means 
        # that there are no triples of repeating numbers in the array and we return -1
        if len(t) == 0:
            return -1

        # Next, using a loop, we check each triple of numbers 
        # (therefore, up to -2 elements)
        for i in range(len(t) - 2):

            # It is necessary to check each triple of numbers in turn without step 3, 
            # because the following situation can arise: 122223 and all triples of numbers: 
                # 122 
                # 222 
                # 222 
                # 223 
            # From four identical numbers, two triples can be made, 
            # and using step 3, the correct option can be missed
            if t[i][0] == t[i+1][0] == t[i+2][0]:

                # When we find three identical numbers, we need their indices, 
                # so we create variables in which we write the indices of each number 
                # (previously, these indices were specified by creating a nested array, 
                # where in each subarray the number itself was in the first place, 
                # and its index was in the second)
                indx1 = t[i][1]
                indx2 = t[i+1][1]
                indx3 = t[i+2][1]

                # we find the absolute difference of numbers
                one = abs(indx1 - indx2)
                two = abs(indx1 - indx3)
                three = abs(indx2 - indx3)

                # We calculate the total distance and add the result to the array 
                # containing all the distances of the matching triplets.
                distance = one + two + three
                minimum_distance.append(distance)

        # we return to the minimum distance
        return min(minimum_distance)