#include <stdio.h>

int main()
{
    int a[3][3]={{1,5,3},{5,6,4},{3,5,4}};
    int b[3][3]={{3,1,4},{5,3,5},{4,5,2}};

    int result[3][3];
    for(int x = 0;x<3;x++){
        for(int i = 0; i <3; i++)
        {
            int multiple = 0,j;
            for(j = 0; j<3; j++)
            {
                multiple = multiple + a[x][j]*b[j][i];
            }

            result[x][i]=multiple;
        
        }
    }

    for(int i = 0;i<3;i++)
    {
        for (int j = 0;j<3;j++)
        {
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }
    return 0;
}