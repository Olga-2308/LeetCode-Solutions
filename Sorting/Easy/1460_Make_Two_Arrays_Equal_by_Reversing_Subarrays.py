class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        '''
        Since the number of permutations is unlimited, it is always possible to create an array equal to the original. 
        It is only impossible to create an array if the elements of the arrays are different.
        '''

        # We sort arrays to determine their equality.
        target.sort()
        arr.sort()

        # If the arrays are equal after sorting, then the elements are the same 
        # and the arrays can be made equal in an unlimited number of steps. 
        # If the arrays are not equal, then there are different elements and it is impossible to create equal arrays.
        return target == arr