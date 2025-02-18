def maximum_sum(arr:list):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
            
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
            
    return[[ max_sum], arr[start:end + 1]]

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
ans = maximum_sum(nums)
print(ans)