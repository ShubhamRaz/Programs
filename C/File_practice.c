#include <stdio.h>

int main(){
    FILE *ptr;

    ptr = fopen("pattern.c","r");


    // fseek(ptr, 0, SEEK_SET);

    // char A[100];
    // while(fgets(A,sizeof(A),ptr) != NULL){
    //     printf("%s",A);
    // }

    char a;

    // fseek(ptr,0,SEEK_SET);

    a = fgetc(ptr);

    while(a!=EOF){
        putchar(a);
        a = fgetc(ptr);
    }

   

    fclose(ptr);
}