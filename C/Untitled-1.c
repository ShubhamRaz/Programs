#include <stdio.h>
int main()
{
    int num;
    int Start;
    int num2;
    printf("Enter a number: ");
    scanf("%d%d", &num,&num2);      // You type: 10<Enter>
    printf("Enter Number:");
    scanf("%d", &Start);    // Immediately reads the leftover newline, '\n'

    printf("%d %d %d",num,Start,num2);

    return 0;
}