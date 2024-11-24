#include <stdio.h>
int main()
{
    int a = 34;
    int* b = &a;
    *b = 25;
    printf("%d",a);

    int Arr[]={2,5,4,6,80};
    
    printf("%d\n",&Arr[0]);
    printf("%d\n",Arr[0]);
    printf("%d\n",Arr);
    printf("%d\n",Arr+1);

    return 0;
}