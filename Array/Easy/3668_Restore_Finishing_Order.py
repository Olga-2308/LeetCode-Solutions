class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        
        # Create an empty list to add friends in the correct order.
        result = []

        # We create a loop in which we check each number from the list.
        for num in order:

            # If a number from the ordinal list is available to one of the friends in another list, 
            # then we add this number to the list
            if num in friends:
                result.append(num)

        return result