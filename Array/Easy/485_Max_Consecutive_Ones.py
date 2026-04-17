class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        '''
        We create variables with zero values ​​to calculate the final and current results, respectively.
        '''
        result = 0
        counter = 0

        '''
        We create a loop in which we count a sequence of continuous 1s in the array. 
        As soon as we encounter another 1, we increment the counter by 1.
        '''
        for num in nums:
            if num == 1:
                counter += 1

                '''
                After each new unit, we update the overall result if it becomes greater than the current one.
                As soon as we find 0, the sequence is terminated and the counter is reset to zero for further correct counting of the next sequence 1
                '''
                if counter > result:
                    result = counter
            else:
                counter = 0

        return result