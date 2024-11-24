#include <stdio.h>
int main()
{
    FILE *ptr = NULL;
    ptr = fopen("Myfile.txt","w+");
    // char c = fgetc(ptr);
    // printf("%c",c);

    fputs("Hello,I am Shubham",ptr);
    fseek(ptr, 0, SEEK_SET); 
    

    char A[10];
    fgets(A,10,ptr);
    printf("%s",A);



    


    fclose(ptr);
    return 0;
}