## minimum insertion required to make a string palindrome
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    rev = s[::-1]

    # dp[i][j] = LCS length of s[0..i-1] and rev[0..j-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


def minInsertionsForPalindrome(s: str) -> int:
    return len(s) - longestPalindromeSubseq(s)


print(longestPalindromeSubseq("abcaa"))     # 3
print(minInsertionsForPalindrome("abcaa"))  # 2

## valid anagrams
def anagrams(s1, s2):
    if len(s1) != len(s2):
      return False

    count = [0]*256  # Assuming ASCII character set

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for c in count:
        if c != 0:
            return False
    return True

print (anagrams("listen", "silent"))  # True

## count and say
# Function to generate the nth term of the count-and-say sequence
def countAndSay(n):
    result = "1"

    # Generate the sequence up to the nth term
    for _ in range(1, n):
        current = ""
        count = 1

        # Traverse the previous result
        for j in range(1, len(result)):
            # If current character matches previous, increment count
            if result[j] == result[j - 1]:
                count += 1
            else:
                # Append count and character to current result
                current += str(count) + result[j - 1]
                count = 1

        # Append the last group
        current += str(count) + result[-1]

        # Update result for next iteration
        result = current

    # Return the final result
    return result

# Call the function and print the result
n = 5
print("Count and Say term", n, ":", countAndSay(n))