#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int Random(int a)
{
    srand(time(NULL));
    return rand() % a;
}

int main()
{
    char a;
    printf("\033[34mRock - R\nPaper - P\nScissor - S\033[0m\n");
    int n = 1;

    int PC = 0, You = 0, Draw = 0;

    while (n <= 5)
    {
        printf("\033[1;33mRound %d\n\033[0m", n);
        printf("\033[36mEnter: \033[0m");
        scanf(" %c", &a);

        if (Random(3) == 0 && a == 'R')
        {
            printf("\033[31mRock  Rock\033[0m\n");
            Draw++;
        }

        else if (Random(3) == 1 && a == 'P')
        {
            printf("\033[31mPaper  Paper\033[0m\n");
            Draw++;
        }

        else if (Random(3) == 2 && a == 'S')
        {
            printf("\033[31mScissor   Scissor\033[0m\n");
            Draw++;
        }

        else if (Random(3) == 0 && a == 'S')
        {
            printf("\033[32mRock \033[31m Scissor\033[0m\n");
            PC++;
        }

        else if (Random(3) == 0 && a == 'P')
        {
            printf("\033[31mRock  \033[32mPaper\033[0m\n");
            You++;
        }

        else if (Random(3) == 1 && a == 'R')
        {
            printf("\033[32mPaper \033[31m Rock\033[0m\n");
            PC++;
        }

        else if (Random(3) == 1 && a == 'S')
        {
            printf("\033[31mPaper \033[32m Scissor\033[0m\n");
            You++;
        }

        else if (Random(3) == 2 && a == 'P')
        {
            printf("\033[32mScissor \033[31m Paper\033[0m\n");
            PC++;
        }

        else if (Random(3) == 2 && a == 'R')
        {
            printf("\033[31mScissor \033[32m Rock\033[0m\n");
            You++;
        }

        else
        {
            printf("\033[34mRock - R\nPaper - P\nScissor - S\033[0m\n");
            continue;
        }

        n++;
    }

    printf("\033[1;33mYou Scored: %d\nPC Scored: %d\nDraw: %d\033[0m", You, PC, Draw);

    return 0;
}
