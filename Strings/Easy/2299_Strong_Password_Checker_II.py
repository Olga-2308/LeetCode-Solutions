class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        '''
        We need to check whether the string meets all the listed conditions. 
        Since the conditions are for characters, we check each character in turn in a loop to see if it meets one of the conditions. 
        If the string doesn't meet any of the conditions, we return false.
        '''

        special_chars = "!@#$%^&*()-+"

        # create counters for each of the conditions that will determine the truth or falsity of the conditions
        count_low, count_upper, count_digit, count_special = 0, 0, 0, 0

        # First, we check the password length and terminate the password check if the length is shorter than the set one.
        if len(password) < 8:
            return False

        # In the loop, we check each character against one of the conditions. 
        # As soon as a character matches one of the conditions, the corresponding counter is incremented. 
        # Since the loop checks pairs of characters, we shift the boundary by one to the left to avoid going beyond the boundary.
        for i in range(len(password)-1):

            if password[i] == password[i+1]:
                return False
            elif password[i].islower():
                count_low += 1
            elif password[i].isupper():
                count_upper += 1
            elif password[i].isdigit():
                count_digit += 1
            elif password[i] in special_chars:
                count_special += 1

        # check the last character of the password separately, since it was excluded from the loop.
        if password[-1].islower():
            count_low += 1
        elif password[-1].isupper():
            count_upper += 1
        elif password[-1].isdigit():
            count_digit += 1
        elif password[-1] in special_chars:
                count_special += 1

        # The password is only suitable if all conditions are met
        return count_low > 0 and count_upper > 0 and count_digit > 0 and count_special > 0