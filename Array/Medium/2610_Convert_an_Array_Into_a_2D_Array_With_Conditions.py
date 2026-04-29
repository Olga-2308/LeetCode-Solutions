class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        d = {}

        # Using a dictionary, we write down the number of each character in the array.
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        # To determine how many arrays we'll need, we need to determine the maximum frequency. 
        # This will be the minimum number of lists required.
        c = d.values()
        count = max(c)

        res = []

        # Using a loop, we create empty lists, the number of which is equal to the maximum frequency value
        for i in range(count):
            res.append([])

        # We create a loop in which we iterate the key and value of the element using the method
        for key, value in d.items():

            # We create a loop in which we add each element the number of times specified in the frequency value.
            for i in range(value):
                res[i].append(key)

        return res