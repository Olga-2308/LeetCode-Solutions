class Solution:
    def countSeniors(self, details: List[str]) -> int:

        # create a counter to count the number of people
        counter = 0

        # create a loop in which we work with each line in order
        for det in details:

            # (!) redundant, one cycle is enough
            for i in range(1):

                # the passenger's age consists of two characters, numbers 12 (index 11) and 13 (index 12)
                age = det[11] + det[12]
 
                # convert the string into a number and compare it with the age. 
                # If the condition is met, we increase the counter by 1.
                if int(age) > 60:
                    counter += 1

        return counter