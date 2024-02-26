class Solution(object):
    def intToRoman(self, num):
        romanDictionary = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        romanValue = ''
        temp = num
        for symbol, value in romanDictionary:
            while temp >= value:
                romanValue += symbol
                temp -= value

        return romanValue
