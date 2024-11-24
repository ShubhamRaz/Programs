// #include <stdio.h>
// #include <string.h>  // Include this header for string handling functions

// int main()
// {
//     char First[100], Second[100];  // Declare arrays to hold the strings

//     // Input first string
//     printf("Enter 1st String: ");
//     scanf("%s", First);  // Use %s to read a string into the First array
    
//     // Input second string
//     printf("Enter 2nd String: ");
//     scanf("%s", Second);  // Use %s to read a string into the Second array

//     // Check if lengths of the strings are the same
//     if(strlen(First) == strlen(Second)){
//         int n = 0;
//         for(int i = 0; i < strlen(First); i++){
//             if(First[i] != Second[i]){
//                 printf("Strings are not equal!\n");
//                 n = 1;
//                 break;
//             }
//         }

//         if(n == 0){
//             printf("Strings are Equal\n");
//         }
//     }
//     else{
//         printf("Length of Strings is not the same!\n");
//     }

//     return 0;
// }


// 3. Write a program to reverse each word in a given sentence while keeping the word order intact. For example, "Hello World" should become "olleH dlroW".

#include <stdio.h>
int main()
{
    printf("Size: %lu Bytes ",sizeof(int));
    return 0;
}

// #include <stdio.h>

// int main() {
//     printf("Size of int: %lu bytes\n", sizeof(int));
//     return 0;
// }
