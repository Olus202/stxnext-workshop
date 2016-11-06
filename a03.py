def palindrome(word):
    """
    Check if the word is a palindrome.
    """
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("abcbaa"))
print(palindrome("abcba"))
