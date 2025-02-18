def two_sum(arr:list , target):
    dict = {} 
    for i , num in enumerate(arr):
        com = target - num
        if com in dict:
            print(f"{dict[com]} and {i}")
            
        dict[num] = i
        
    
nums = [2, 7, 11, 15]
target = 9
print("Two Sum Indices:", two_sum(nums, target))