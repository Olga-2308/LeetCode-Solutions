class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        We need to determine whether an array contains two numbers at different indexes that satisfy the problem condition. 
        Using a nested loop, we check for pairs of numbers, and if such a pair is found, we immediately return true and terminate the loop.
        '''

        for i in range(len(arr)):
            # We shift the inner loop by 1 to avoid repeated checks
            for j in range(i+1, len(arr)):
                # As soon as we find a pair of numbers that meet the conditions of the problem, we return true and end the loop.
                if i != j:
                    if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                        return True

        return False