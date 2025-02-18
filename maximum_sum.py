def maximum_sum(arr:list):
    max_sum = float('-inf')
    current_sum = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
            
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
nums = [5,4,-1,7,8]
ans = maximum_sum(nums)
print(ans)