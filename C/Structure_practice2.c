#include <stdio.h>

struct student
{
    int id;
    char name[20];
    char course[20];
    int fees;

};

void Display(int id,char *name, char *course, int fees)
{
    printf("ID: %d\nName: %s\nCourse: %s\nFEES: %d",id,name,course,fees);
}

void Display2(struct student *b)
{
    printf("ID: %d\nName: %s\nCourse: %s\nFEES: %d",b->id,b->name,b->course,b->fees);
}

int main()
{
    struct student Stud1 = {1,"Shubham","B-tech",250000};

    // printf("%d",Stud1.fees);

    // Display(Stud1.id,Stud1.name,Stud1.course,Stud1.fees);

    Display2(&Stud1);
}