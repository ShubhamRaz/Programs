#include <stdio.h>

typedef struct Name
{
    char first[20];
    char mid[20];
    char last[20];
}Name;

typedef struct student
{
    int id;
    Name name;
    int age;
}Student;

int main()
{
    Student student1={1,{"Pankaj","Kumar","Raj"},18};

    printf("%s",student1.name.last);
}