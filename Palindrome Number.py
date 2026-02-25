class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Reverses the integer mathematically and compares it to the original.
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
            
        original = x
        reversed_num = 0
        
        while x > 0:
            # Extract the last digit
            digit = x % 10
            # Append the digit to the reversed number
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from the original number using integer division
            x //= 10
            
        return original == reversed_num