#include <stdio.h>
int main()
{
    int num;
    printf("Enter a Number: ");
    scanf("%d",&num);

    printf("Number %d is: %s",num,(num%2==0? "Even": "Odd"));

    return 0;
}