def find_missing_num(arr:list):
    n = max(arr)
    total  = n * (n + 1) // 2
    
    return total - sum(arr)

nums = [1, 2, 4, 5, 6]
n = 6
print("Missing Number:", find_missing_num(nums))