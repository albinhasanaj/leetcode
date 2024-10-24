class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w = len(word1)
        ww = len(word2)
        
        new_str = ""
        for idx, char in enumerate(word1):
            new_str += char + word2[idx]
            if w < ww and idx == w-1:
                new_str+= word2[idx+1:]
                break
            if w > ww and idx == ww-1:
                new_str+= word1[idx+1:]
                break

        return new_str

# Example usage:
solution = Solution()

# Test Case 1
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqcr"

# Test Case 2
word1 = "ab"
word2 = "pqrs"
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqrs"

# Test Case 3
word1 = "abcd"
word2 = "pq"
print(solution.mergeAlternately(word1, word2))  # Expected output: "apbqcd"

# Test Case 4
word1 = "x"
word2 = "yz"
print(solution.mergeAlternately(word1, word2))  # Expected output: "xyz"

# Test Case 5
word1 = "hello"
word2 = "world"
print(solution.mergeAlternately(word1, word2))  # Expected output: "hweolrllod"

