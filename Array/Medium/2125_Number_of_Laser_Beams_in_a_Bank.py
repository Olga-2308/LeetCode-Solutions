class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        device = []

        # We count the number of lasers in each row and create an array of numbers
        for b in bank:

            # If there are no lasers in the row, then skip the line, as it will not be needed in the future.
            if "1" not in b:
                continue
            else:
                counter = b.count("1")
                device.append(counter)

        total = 0

        # To find the number of intersections between lasers from two rows, 
        # you need to find their product, and then return the total sum
        for i in range(len(device) - 1):
            pairs = device[i] * device[i+1]
            total += pairs

        return total