class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        # find the sum of numbers from the list
        elements = sum(nums)

        # create a variable to calculate the sum of the digits of numbers from a list.
        digit_sum = 0

        # ''' We need to calculate the sum of the digits of all the numbers in a list. 
        # We create the first loop, working with a list element (number). 
        # We need to find the sum of the digits of this number. 
        # To do this, we create a nested loop in which we will work with this number. 
        # We immediately convert it to a string so that we can iterate over all its characters. 
        # Next, we convert each character to a number and store it in a variable. '''

        for num in nums:
            for char in str(num):
                digit_sum += int(char)

        # find the modulus of the difference
        result = abs(elements - digit_sum)

        return result
    

        ''' Необходимо посчитать сумму цифр всех чисел из списка. 
        Создаем первый цикл (for num in nums), в котором работаем с элементом списка - числом. 
        Нужно найти сумму цифр этого числа. 
        Для этого создаем вложенный цикл (for char in str(num)), в котором будем работать с этим числом. 
        Сразу превратим его в строку (str(num)), чтобы можно было перебирать все его символы. 
        Далее каждый символ превращаем в число и складываем в переменную (+= int(char)) '''