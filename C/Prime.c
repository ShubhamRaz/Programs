#include <stdio.h>
int main()
{
    
    for(int a = 2; a<=100; a++){
        int temp = 0;
        for(int b = 2; b<=a/2; b++){
            if (a%b==0){
                temp++;
                break;
            }
            
        }

        if (temp ==0){
            printf("\033[3m%d\n\033[0m",a);
        }
    }

    printf("Done!");
    return 0;
}