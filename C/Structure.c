#include <stdio.h>
#include <string.h>
struct Student{
    int ID;
    char name[35];

};

int main()

{
    struct Student Pankaj, Shubham;
    Pankaj.ID =1;
    strcpy(Pankaj.name,"Pankaj Kumar\n");

    Shubham.ID = 2;
    strcpy(Shubham.name,"Shubham Raj\n");
    

    printf("ID: %d\nName: %s",Pankaj.ID,Pankaj.name); 
    printf("ID: %d\nName: %s",Shubham.ID,Shubham.name);
    
    return 0;
}