#include <stdio.h>

// int Rec(int a)
// {
//     if (a < 1)
//     {
//         return 1;
//     }

//     else
//     {
//         return a * Rec(a - 1);
//     }
// }

// int main()
// {


int main()

{
    int a = 5;
    int *b;
    b = &a;

    

    printf("%d\n",b);
    printf("%u\n",&b);
    printf("%u\n",a);
    printf("%u",&a);
    

}






    // printf("%d", Rec(1));
// }