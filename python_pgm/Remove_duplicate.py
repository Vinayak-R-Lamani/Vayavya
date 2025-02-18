def remove_duplicate(string:str):
    dict = {}
    for i in string:
        # if i in dict:
        #     dict[i] += 1
        # else:
        #     dict[i] = 1
            
        dict[i] = dict.get(i , 0)+1
    ans = ''.join([i for i in string if dict[i] == 1])
    print(ans)
    
s = "aabbccdeff"
remove_duplicate(s)