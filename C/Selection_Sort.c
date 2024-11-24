#include <stdio.h>
void Sort(int *Array, int size)
{
    for(int i = 0;i<size-1;i++)
    {
        int MinIndex = i;
        for(int j = i+1;j<size;j++)
        {
            if(Array[j]<Array[MinIndex])
            {
                MinIndex = j;
            }
            
        }

        int temp = Array[i];
        Array[i]=Array[MinIndex];
        Array[MinIndex]=temp;
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