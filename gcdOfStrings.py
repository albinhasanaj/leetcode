class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))
        
        return str1[:gcd_length]

# Example usage:
solution = Solution()

# Test Case 1
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))  # Expected output: "ABC"

# Test Case 2
str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))  # Expected output: "AB"

# Test Case 3
str1 = "LEET"
str2 = "CODE"
print(solution.gcdOfStrings(str1, str2))  # Expected output: ""
