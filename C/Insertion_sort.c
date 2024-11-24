#include <stdio.h>

void Sort(int *A, int size)
{
    for(int i = 1; i<size; i++)
    {
        int Current = A[i];
        int j = i-1;

        while(A[j]>Current && j>=0)
        {
            A[j+1]=A[j];
            j--;
        }

        A[j+1]=Current;
    }
}


int main()
{
    int a[]={3,5,2,1,7,6,4};
    int size=sizeof(a)/sizeof(int);
    Sort(a,size);

    for(int i = 0;i<size;i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}