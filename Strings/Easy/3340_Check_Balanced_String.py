class Solution:
    def isBalanced(self, num: str) -> bool:

        # create variables in which we calculate the sum of numbers under odd and even indices
        odd = 0
        even = 0

        # create a loop in which we go through all the numbers and their indices in order
        for i in range(len(num)):

            # If the index is even, then we convert the string symbol into a digit and add it to the total sum of numbers
            if i % 2 == 0:
                even += int(num[i])
            
            # otherwise, we convert the string symbol into a digit and add it to the total sum of numbers with odd indices
            else:
                odd += int(num[i])

        # If the sum of the numbers under the even indices is equal to the sum of the numbers under the odd indices, 
        # then return true, otherwise return false
        return odd == even
