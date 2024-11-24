#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *ptr = malloc(5*sizeof(int));
    // printf("%d",ptr);
    for(int a = 0;a<5;a++){
        ptr[a]=a+1;
    }

    for(int b = 0; b<5;b++){
        printf("%d\n",*ptr+b);
    }

    // free(ptr);
    ptr = realloc(ptr,10*sizeof(int));

    if(ptr == NULL){
        printf("Memory Allocation faild!");
    }

    for(int a = 5;a<10;a++){
        ptr[a]=a+1;
    }

    for(int b = 0; b<10;b++){
        printf("%d\n",*ptr+b);
    }


    free(ptr);

    // if(ptr != NULL){
    //     printf("Not Null!\n");
    // }

    // for(int a = 0;a<10;a++){
    //     ptr[a]=a+1;
    // }

    // for(int b = 0; b<10;b++){
    //     printf("%d\n",*ptr+b);
    // }


    return 0;
}