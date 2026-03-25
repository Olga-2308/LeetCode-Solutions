class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        # revers the line
        new_num = num[::-1]

        # If the new line does not start with 0, then we return num
        if new_num[0] != '0':
            return num

        # ''' otherwise, we remove all 0's from the left of the new string using the method, 
        # reverse the resulting string and return it to the result '''
        else:
            res = new_num.lstrip('0')
            result = res[::-1]
            return result
        



# class Solution:
#   def removeTrailingZeros(self, num: str) -> str:
#       return num.rstrip('0') - Using the method, we return a string without the leading 0 on the right.