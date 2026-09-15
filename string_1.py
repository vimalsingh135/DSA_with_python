## Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        
        # Pointer starting from end
        i = len(s) - 1
        
        # Traverse from right to left
        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            # If pointer out of bounds, break
            if i < 0:
                break
            
            # Mark end of word
            end = i
            
            # Move left until space or start
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # Extract the word
            word = s[i + 1:end + 1]
            
            # Add space if result is not empty
            if result != "":
                result += " "
            
            # Append word
            result += word
        
        return result

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))


## Longest Palindromic Substring
def longest_palindrome(s):
    n=len(s)
    if n==0:
        return ""

    start=0
    max_lenght=1

    for i in range(1, n):
        # Even length palindrome
        low=i-1
        high=i
        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1>max_lenght:
                start=low
                max_lenght=high-low+1
            low-=1
            high+=1

        # Odd length palindrome
        low=i-1
        high=i+1
        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1>max_lenght:
                start=low
                max_lenght=high-low+1
            low-=1
            high+=1

    return s[start:start+max_lenght]
print ("the longest palindromic substring is :", longest_palindrome("babad"))
print ("the longest palindromic substring is :", longest_palindrome("cbbdkkanabidabcasasasasa"))

## Roman Numerals to Integer
def roman_to_integer(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_dict[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

print("The integer value of the Roman numeral is:", roman_to_integer("III"))
print("The integer value of the Roman numeral is:", roman_to_integer("IV"))
print("The integer value of the Roman numeral is:", roman_to_integer("IX"))
print("The integer value of the Roman numeral is:", roman_to_integer("LVIII"))
print("The integer value of the Roman numeral is:", roman_to_integer("MCMXC"))


## Longest Common Prefix
class Solution:
    # Returns the longest common prefix from a list of strings
    def longestCommonPrefix(self, strs):
        # Handle empty list case
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)

# Run the function with sample input
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()
    
    # Input list of strings
    input_strs = ["interview", "internet", "internal", "interval"]
    
    # Call the method to find prefix
    result = solution.longestCommonPrefix(input_strs)
    
    # Print the result
    print("Longest Common Prefix:", result) 