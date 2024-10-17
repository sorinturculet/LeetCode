from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        c = chars[0]
        repeating = 1
        index = 0  # Use index to keep track of position in the original list

        for i in range(1, len(chars)):
            if chars[i] == c:
                repeating += 1
            else:
                chars[index] = c  # Update the character
                index += 1  # Move to the next position
                if repeating > 1:
                    for digit in str(repeating):  # Append each digit of the count
                        chars[index] = digit
                        index += 1
                c = chars[i]  # Update the current character
                repeating = 1  # Reset count for new character

        # Handle the last character
        chars[index] = c
        index += 1
        if repeating > 1:
            for digit in str(repeating):
                chars[index] = digit
                index += 1

        # Return the length of the compressed list
        return index


# Test the function
result = Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
print(result)  # Output: 4
