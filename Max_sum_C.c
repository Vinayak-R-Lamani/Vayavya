#include <stdio.h>
#include <limits.h>

int maximum_sum(int arr[],int size){
    int max_sum = INT_MIN;
    int cur = 0;
    for(int i = 0; i < size ; i ++){
        cur += arr[i];
        if (cur > max_sum ){
            max_sum = cur;
        }
        if (cur  < 0){
            cur = 0;
        }
    }
    return max_sum;

}

int main(){
    int size;
    printf("Enter the size of the array");
    scanf("%d" , &size);

    int arr[size];
    printf("enter %d element:",size);
    for(int i = 0; i< size;i++){
        scanf("%d",&arr[i]);
    }

    int ans = maximum_sum(arr,size);
    printf("Maximum subarray sum :%d \n ", ans);
    return 0;
}