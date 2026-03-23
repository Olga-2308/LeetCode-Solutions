class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        # First, let's check if a triangle can be formed from the given numbers. If not, then we return 'none'
        if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]):
            return 'none'

        # Let's check the equality of the three sides of the triangle. If all three sides are equal, then the triangle is equilateral.
        if nums[0] == nums [1] and nums[0] == nums [2] and nums[1] == nums [2]:
            return 'equilateral'
        
        # In the next condition we check if there are two identical numbers, if so, the triangle is isosceles
        elif nums[0] == nums [1] or nums[0] == nums [2] or nums[1] == nums [2]:
            return 'isosceles'
        # If the conditions of equality of three or two sides are not met, then the triangle is scalene
        else:
            return 'scalene'
        
# (!) ''' The condition for checking whether the three sides of a triangle are equal can be stated at the beginning. 
# If the three sides are equal, then it is an equilateral triangle, 
# and there is no need to check whether the lengths of its sides allow one to form this triangle. '''