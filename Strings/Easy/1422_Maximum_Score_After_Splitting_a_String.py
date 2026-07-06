class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0
        l = len(s)

        # using a loop we begin to form substrings at each iteration
        for sub in range(1, l):

            # we determine the right and left slices at the current iteration
            left = s[:sub]
            right = s[sub:]

            # we set up counters of ones and zeros
            count_0 = 0
            count_1 = 0

            # on the left side we use a loop to count 0
            for char in left:
                if char == '0':
                    count_0 +=1

            # on the right side we count 1
            for char in right:
                if char == '1':
                    count_1 +=1

            # we find the general result
            score = count_0 + count_1

            # we determine the maximum value
            if score > max_score:
                max_score = score

        return max_score  