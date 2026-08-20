## Print All Permutations of a String/Array
def permute(s):
    result = []
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
            return
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]  # Swap
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]  # Backtrack (swap back)

    backtrack(0)
    return result