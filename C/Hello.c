#include <stdio.h>

// // Correct function signature for main
// int main(int argc, char const *argv[])
// {
//     printf("Hello World\n");
//     return 0;
// }

// int main()
// {
//     int a,b;
//     printf("Enter num a: ");
//     scanf("%d",&a);
//     printf("Enter num b: ");
//     scanf("%d",&b);

//     printf("The sum is: %d",a+b);
    

//     return 0;
// }


// int main(){
//     float a;
//     float b;
//     a=20.1;
//     b=10.5;
//     printf("The sum is %d\n",a+b);
//     printf("The diff is %d\n",a-b);
//     printf("The mul is %d\n",a*b);
//     printf("The div is %d\n",a/b);

// }

// int main()

// {
//     printf("Enter Number: ");
//     int a;
//     scanf("%d",&a);
    // printf("%d x 1 = ",a);
    // printf("%d\n",a*1);
    // printf("%d x 2 = ",a);
    // printf("%d\n",a*2);
    // printf("%d x 3 = ",a);
    // printf("%d\n",a*3);
    // printf("%d x 4 = ",a);
    // printf("%d\n",a*4);
    // printf("%d x 5 = ",a);
    // printf("%d\n",a*5);
    // printf("%d x 6 = ",a);
    // printf("%d\n",a*6);
    // printf("%d x 7 = ",a);
    // printf("%d\n",a*7);
    // printf("%d x 8 = ",a);
    // printf("%d\n",a*8);
    // printf("%d x 9 = ",a);
    // printf("%d\n",a*9);
    // printf("%d x 10 = ",a);
    // printf("%d\n",a*10);

// }



// int main(){
//     int a = 5;
//     float b = 10.4;

//     int c;
//     printf("Enter Value of c: ");
//     scanf("d",&c);

//     printf("The value of a is %d \nThe value of b is %f \nThe value of c is %d\n",a,b,c);
//     printf("Float edit: %8.3f",b);
// }


//Calculater 

int main()
{
    int num1,num2;
    char o;
    printf("Enter Number 1: ");
    scanf("%d",&num1);

    printf("Enter Operator: ");
    scanf(" %c",&o);

    printf("Enter Number 2: ");
    scanf("%d",&num2);

    switch (o){
        case '+':
        printf("The sum is %d",num1+num2);
        break;

        case '-':
        printf("The difference is %d",num1-num2);
        break;

        case '*':
        printf("The multiple is %d",num1*num2);
        break;

        case '/':
        printf("The division is %d",num1/num2);
        break;

        default:
        printf("Operator not found");
        break;
        

    }
    

}




// int main()
// {
//     int num1, num2;
//     char o;

//     printf("Enter Number 1: ");
//     scanf("%d", &num1);

//     // Adding a space before %c to handle any leftover newline character in the input buffer
//     printf("Enter Operator (+, -, *, /): ");
//     scanf(" %c", &o);

//     printf("Enter Number 2: ");
//     scanf("%d", &num2);

//     switch (o) {
//         case '+':
//             printf("The sum is %d\n", num1 + num2);
//             break;

//         case '-':
//             printf("The difference is %d\n", num1 - num2);
//             break;

//         case '*':
//             printf("The product is %d\n", num1 * num2);
//             break;

//         case '/':
//             if (num2 != 0) {
//                 printf("The division result is %.2f\n", (float)num1 / num2);  // Casting to float for correct division
//             } else {
//                 printf("Error: Division by zero is not allowed\n");
//             }
//             break;

//         default:
//             printf("Operator not recognized\n");
//             break;
//     }

//     return 0;
// }
