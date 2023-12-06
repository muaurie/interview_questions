class Solution :    
    def romantoInt(self, s: str) -> int:
        roman = {"I": 1, "IV": 4,"V": 5,"IV": 9,"X": 10,"XL": 40,"L": 50, "XC": 90,"C": 100, "CD": 400, "D": 500, "CM": 900,"M": 1000}
        ##nested list, list of smaller list where the symbol is mapped to the int.
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i +1]]:
                res -= roman[s[i]]
            else:
                res += roman [s[i]]
        return res