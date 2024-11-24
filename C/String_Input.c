#include <stdio.h>
int main()

{
    char A[]="Hello World";
    printf("Enter String: ");
    char B[100];
    scanf("%s",B);

    char C[100];
    printf("Enter String: ");
    gets(C);
    fgets(C,sizeof(C),stdin);
    printf("%s",C);

    int X,Y,Z;

    scanf("%d%d%d",&X,&Y,&Z);
    printf("%d%d%d",X,Y,Z);


}