#include <stdio.h>
#include <limits.h>
#include <stdbool.h>
#include <string.h>
bool isPalindrome(char str[] , int left , int right){   
    while ( left < right)
    {
        /* code */
        if (str[left] != str[right]){
            return false;
        }
        left ++;
        right --;
    }
    return true;
    
}


void findPalindromicSubstring(char str[]){
    int len = strlen(str);
    for(int i = 0; i< len ;i++){
        for(int j = i ; j < len ; j++){
            if( isPalindrome(str, i , j)){
                for(int k  = i ; k <= j ; k ++){
                    printf("%c" , str[k]);
                }
                printf("\n");
            }
        }
    }
}

int main(){
    char str[100];
    printf("enter the string: ");
    // scanf("%s" , str);
    gets(str);
    findPalindromicSubstring(str);
    return 0;
}