def is_palindrome(string:str):
    return string == string[::-1]

def find_palindromic_substring(string:str):
    palindrome = []
    
    for i in range(len(string)):
        for j in range(i + 1 , len(string) +1):
            if is_palindrome(string[i : j +1]):
                palindrome.append(string[i:j + 1])
                
    return palindrome


def Return_palindrome(string:str):
    palindrome = []
    n = len(string)
    
    def expand_around_center(left , right):
        while left >= 0 and right < n and string[left] == string[right]:
            # if len(string[left:right + 1]) > 1:
            palindrome.append(string[left:right + 1])
            left -= 1
            right += 1
            
    for i in range(n):
        expand_around_center(i , i)
        expand_around_center(i , i + 1)
        
    return palindrome


s = "abba"
print("Palindromic Substrings:", Return_palindrome(s))