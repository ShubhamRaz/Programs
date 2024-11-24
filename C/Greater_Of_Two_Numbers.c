#include <stdio.h>
int main()
{
    int a,b;
    printf("Enter Number: ");
    scanf("%d%d",&a,&b);
    printf("%d is Greater than %d",(a>b?a:b),(b<a?b:a)); 
    return 0;
}