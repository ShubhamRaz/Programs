#include <stdio.h>
#include <stdlib.h>
int main()
{
    // int n;
    // printf("Enter Number: ");
    // scanf("%d",&n);
    // char *min = n%2==0? "even":"odd";
    // printf("%s",min);

    char *a = "Pankaj";
    

    char b[6]="hello";

    char *c = (char *) malloc(100*sizeof(char));
    scanf("%s",c);

    printf("%s",c);

    free(c);

    // printf("%s %s %s",a,b,c);
    return 0;
}