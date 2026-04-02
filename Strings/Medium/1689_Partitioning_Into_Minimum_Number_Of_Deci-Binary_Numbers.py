class Solution:
    def minPartitions(self, n: str) -> int:
        
        return int(max(n))
    
# According to the problem statement, we need to convert a decimal number 
# into a deci-binary number in the minimum number of deci-binary numbers.
# 
# Let's assume we have some decimal number:
# 
#   12345
# 
# The smallest deci-binary number we can add is 1
# 
#   00001
# 
# The maximum number is obtained:
#
#   11111
# 
# It turns out that with each new addition of a deci-binary number, the decimal place of the number increases by 1.
# 
# It follows that to obtain, for example, the number 4 in a decimal number, 
# a minimum of 4 deci-binary numbers will be required, 
# where the corresponding digit of the decimal number will increase by 1 each time (in total by 4 units)
# 
# It can be argued that to obtain any digit of a decimal number, a corresponding number of deci-binary numbers is required.
# 
# Therefore, to solve this problem, it is necessary to find the maximum digit of a decimal number, 
# because if the number is less than the maximum, 
# then there will not be enough deci-binary numbers to reach the maximum digit in the number.