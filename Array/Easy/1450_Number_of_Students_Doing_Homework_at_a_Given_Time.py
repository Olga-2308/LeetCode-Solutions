class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        # create a counter for the number of students
        counter_students = 0

        # create a loop in which we check the start and end time of each student.
        for i in range(len(startTime)):

            # If the student completes the homework at the specified time, then increase the counter by 1
            if startTime[i] <= queryTime <= endTime[i]:
                counter_students += 1

        return counter_students