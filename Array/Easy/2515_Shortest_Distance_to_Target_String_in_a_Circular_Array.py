class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        '''
        It is possible to immediately determine all occurrences of the desired number in one pass 
        through the loop and write the indices into an array, without allocating memory for a dictionary
        '''

        d = {}

        # We create a dictionary and write into it all occurrences of each word in the array
        for i in range(len(words)):
            if words[i] not in d:
                d[words[i]] = [i]
            else:
                d[words[i]].append(i)

        # If the target word is not in the dictionary, then we immediately return -1
        if target not in d:
            return -1

        min_dist = float('inf')
        l = len(words)

        # we define an array of indices under the numbers of which the target word is located
        nums = d[target]

        # using a loop we check the distance between the starting index and each found occurrence of the word
        for num in nums:

            # Since the array is circular, there are two possible ways to determine the distance between elements. 
            # Let's find the first distance, which is a straight line.
            diff = abs(startIndex - num)

            # After this, we determine the minimum value between the current value, 
            # between the forward direction and between the reverse direction, 
            # which is found as the difference between the length of the array and the forward direction, 
            # the remainder of the length of the circular array is the inverse distance
            min_dist = min(min_dist, diff, l - diff)

        return min_dist
        