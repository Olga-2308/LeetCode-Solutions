class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # create an empty list for a sequence of elements
        result = []

        # ''' check each element of the sequence
        # for each element the code is executed according to the condition 
        # if the number does not meet the conditions above, 
        # then it is added to the list as a string, which is required from the problem conditions'''
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))

        return(result)