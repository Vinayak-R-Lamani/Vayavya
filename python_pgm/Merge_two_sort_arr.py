def merge_two_sort_arr(arr1: list , arr2 : list):
    ans =  []

    m , n = len(arr1) , len(arr2)
    i ,  j   =  0 , 0 

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i +=1 
        else:
            ans.append(arr2[j])
            j +=1 
        
        
        
    while i < m:
        ans.append(arr1[i])
        i += 1
        
    while j < n:
        ans.append(arr2[j])
        j += 1
        
    return ans

def alternative_approach(arr1 , arr2):
    return sorted(arr1 + arr2)

arr1 = [1,6,8]
arr2 = [2,3,4,5,7,9,10]
print("Merged Sorted Array:", alternative_approach(arr1, arr2))