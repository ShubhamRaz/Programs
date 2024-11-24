#include <stdio.h>

struct numbers
{
    int a;
    int b;
    int c;
    int largest;
};

typedef struct numbers num;

int main()
{
   num num1;

   printf("Enter three numbers: ");

   scanf("%d%d%d",&num1.a,&num1.b,&num1.c);

   if(num1.a>num1.b && num1.a>num1.c)
   {
    num1.largest = num1.a;
   }

   else if(num1.b>num1.a && num1.b>num1.c)
   {
    num1.largest = num1.b;
   }  

   else{
    num1.largest=num1.c;
   }

   printf("Largest number: %d",num1.largest);
}