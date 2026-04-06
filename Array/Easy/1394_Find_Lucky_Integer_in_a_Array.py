class Solution:
    def findLucky(self, arr: List[int]) -> int:

        # create a variable to store the maximum lucky number. 
        # If no such number is found in the array, we return -1, as specified in the problem statement.
        lucky_integer = -1

        # create a loop in which we check each number
        for i in range(len(arr)):

            # determine how many times the current number appears in the array
            num = arr.count(arr[i])

            # a number is lucky if its value is equal to its frequency in the list, 
            # and it is also necessary to determine whether this number is the maximum among the lucky numbers, 
            # and only then update the lucky number variable
            if num == arr[i] and num > lucky_integer:
                lucky_integer = num

        return lucky_integer