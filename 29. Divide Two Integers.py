class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        # Convert to positive (absolute) values to simplify subtraction logic, 
        # using negatives for abs() to handle the -2**31 case correctly in Python 
        # (as abs(-2**31) is 2**31 which overflows 32-bit positive range in C++/Java)
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        ans = 0
        while dvd >= dvs:
            # Find the largest multiple of dvs that is less than or equal to the remaining dvd
            temp = dvs
            multiple = 1
            while dvd >= (temp << 1): # Use left shift to double (multiply by 2)
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple and add to the answer
            dvd -= temp
            ans += multiple
        
        # Apply the determined sign
        return ans if sign == 1 else -ans
