#include <stdio.h>

void Swap(int *a, int *b){
    int Temp;
    Temp = *a;
    *a = *b;
    *b = Temp;
}

int main(){
    int a = 5;
    int b = 10;

    printf("Before Swap: a = %d b = %d\n", a,b);
    Swap(&a,&b);

    printf("After Swap: a = %d b = %d", a,b);
}