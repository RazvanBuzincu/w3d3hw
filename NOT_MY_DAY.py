# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur inside of the list 
# (a palindrome is a word that is spelled the same backwards and forward).

# Example input: ['dog', 'racecar', 'wildebeest']
# Output: 1
# Explanation: 'racecar' is the only palindrome in the list

# Example input: ['kayak', 'level', 'word', 'smooth', 'detartrated']
# Output: 3
# Explanation: 'kayak', 'level', and 'detartrated' are all palindromes


def words(silly_words):
    result = 0
    for palindrome in silly_words:
    # teach the function how to identify a palindrome
        if palindrome == palindrome[::-1]:
            result += 1
    return result
            

print(words(['kayak', 'level', 'word', 'smooth', 'detartrated']))