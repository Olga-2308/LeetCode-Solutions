class Solution:
    def trafficSignal(self, timer: int) -> str:
        '''
        We determine the range of numbers in which the timer is located and display the corresponding string in response.
        '''

        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        else:
            return "Invalid"