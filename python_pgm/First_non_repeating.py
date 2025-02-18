def first_non_repeating_char(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        
    for i , j in dict.items():
        if j == 1:
            return i
    

s = "aabbccdeff"
print("First Non-Repeating Character:", first_non_repeating_char(s))