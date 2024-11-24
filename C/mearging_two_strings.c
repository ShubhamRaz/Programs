#include <stdio.h>
#include<string.h>

int main(){
    for(int i = 10; i<20; i++){
        char a[10]="hii";
        char txt[5]=".txt";
        char *b;

        sprintf(b,"%d",i);

        strcat(a,b);
        strcat(a,txt);

        // FILE *ptr = fopen(a,"w");
        // fclose(ptr);

        remove(a);

        printf("%s\n",a);

        
    }
}