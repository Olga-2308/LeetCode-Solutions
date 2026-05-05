class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        '''
        To find the number of points, you need to determine all the points between the coordinates in each subarray 
        and use the set to return the unique number of points
        '''

        points = []

        for num in nums:

            # Using a nested loop, we generate all the numbers between the coordinates in each subarray 
            # and add all the points to the overall array.
            for i in range(num[0], num[1]+1):
                points.append(i)

        # Using a set, we remove duplicates and return the number of unique points
        return len(set(points))