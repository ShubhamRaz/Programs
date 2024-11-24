#include <Stdio.h>

int Binary(int a){
    int lst[1000];
   
    int i = 0;
    while(a>0){
        int R = a%2;
        a = a/2;
        lst[i]=R;
        i++;
    }

    // printf("Size of lst: %d",sizeof(lst));

    for (int j = i - 1; j >= 0; j--) {
        printf("%d", lst[j]);

    }

}

int main()
{
    char Start = 'A';
    while(Start!='n' && Start!='N'){
    int num;
    printf("Enter Decimal Number: ");
    scanf("%d",&num);
    printf("Binary Number of %d is: ",num);
    Binary(num);

    printf("\nEnter N to Stop: ");
    scanf(" %c",&Start);
    }
    return 0;
}