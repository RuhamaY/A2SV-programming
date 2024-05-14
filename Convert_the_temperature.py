class Solution(object):
    def convertTemperature(self, celsius):
        
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.0
        return [kelvin, fahrenheit]
