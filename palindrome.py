# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

def is_palindrome(s):
    if s == "":        # base case
        return True
    else:
        if s[0] == s[-1]:   # check if first and last letter match
            return is_palindrome(s[1:-1])    # repeat using rest
        else:
            return False


print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True