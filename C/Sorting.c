#include <stdio.h>
//Sor numbers in ascending order
int main()
{
    int List[] = {25,15,36,45,100,12,45,48,75,10};
    int ListSize=sizeof(List)/4;
    

    for(int i = 0; i<ListSize-1; i+=1){
        for(int j = 0; j < ListSize-i-1; j+=1){
            int temp;
            if(List[j]>List[j+1]){
                temp=List[j];
                List[j]=List[j+1];
                List[j+1]=temp;


            }

            
        }

    }
    int n=0;

    while(n<ListSize){
        printf("%d,",List[n]);
        n+=1;
    }
}