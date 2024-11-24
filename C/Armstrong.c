#include <stdio.h>
int main()
{
    int a,y=0;
    
   
    printf("Enter Number: ");
    scanf("%d",&a);

    int b = a;

    while(a>0){
        a = a/10;
        y++;

    }

    a = b;
    int power = y;

    int mul = 1,armst=0;

    while(b>0){
        int temp = b%10;
        b = b/10;

        while(y>0){
            mul = mul*temp;
            y--;
            
        }

        y = power;

        armst = armst + mul;
        mul = 1;

    }

    if (armst == a){
        printf("%d is Armstrong Number",a);
    }

    else{
        printf("%d is Not armstrong Number",a);
    }
    return 0;
}