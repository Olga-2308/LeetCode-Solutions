class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        # We create an array of words from the string, 
        # in which each number is now a separate set of characters
        numbers = s.split()
        num = []

        # Using a loop, we determine which words consist only of numbers 
        # and add them to a separate array
        for number in numbers:
            if number .isdigit():
                num.append(int(number))

        # If the length of the set is not equal to the length of the array, 
        # it means there are duplicates in the array. 
        # And identical numbers cannot be in a strictly increasing sequence.
        if len(set(num)) != len(num):
            return False

        # create a copy of the array and sort it
        n = num.copy()
        n.sort()
  
        # If an array of numbers is equal to a sorted array, 
        # it means that the numbers from the string are in strictly ascending order
        return num == n


        '''
        If numbers can be inside a word 
        (numbers are not separated by spaces on both sides)

        num = ""

        for i in range(len(s) - 1):
            if s[i].isdigit() and s[i+1].isdigit():
                num += s[i]
            elif s[i].isdigit():
                num += s[i] + " "
            else:
                continue

        if s[-1] .isdigit():
            num += s[-1]

        numbers = num.split()
        n = []

        for num in numbers:
            nn = int(num)
            n.append(nn)

        if len(set(n)) != len(n):
            return False

        nn = n.copy()
        nn.sort()
  
        return n == nn
        '''