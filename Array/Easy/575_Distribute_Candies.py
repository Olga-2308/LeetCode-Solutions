class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # we determine how many types of different candies are in the array
        types = set(candyType)

        # Let's determine how many candies Alice can eat.
        half = len(candyType) // 2

        # If there are less unique types than the number allowed by the doctor, 
        # it means that Alice can eat all the unique types
        if len(types) < half:
            return len(types)
        
        # and if there are fewer different types of candy, 
        # then Alice can only eat what the doctor allowed
        else:
            return half