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
