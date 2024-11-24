#include <stdio.h>

int Fun(int *x){
    int avg = *x + *(x+1) + *(x+2) + *(x+3);
    return avg;
}

int main(){
    int arr[]={1,2,3,4};
    int avg = Fun(arr);
    printf("%d",avg);
}