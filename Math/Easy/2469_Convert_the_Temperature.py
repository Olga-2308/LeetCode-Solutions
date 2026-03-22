class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        # create an empty list to which we will add the results obtained
        result = []

        # convert degrees and add the result to the list
        kelvin = celsius + 273.15
        result.append(kelvin)

        # convert degrees and add the result to the list
        fahrenheit = celsius * 1.80 + 32.00
        result.append(fahrenheit)

        return(result)