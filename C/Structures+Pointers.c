#include <stdio.h>
#include <string.h>


struct Student{
        char name[20];
        int ID;
        int age;
    };

void Display(struct Student *b){
    printf("%s %d %d",b->name,b->ID,b->age);
    
}

int main(){
    


    struct Student Shubham,Ashish,Ankur;
    struct Student *ptr;

    strcpy(Shubham.name,"Shubham Raj");
    Shubham.ID=1;
    Shubham.age=18;

    strcpy(Ashish.name,"Ashish Kumar");
    Ashish.ID=2;
    Ashish.age=19;

    strcpy(Ankur.name,"Ankur Kumar");
    Ankur.ID = 3;
    Ankur.age=20;
    
    struct Student Aryan={"Aryan Raj",4,18};

    // printf("%s",Aryan.name);
    // Display(Shubham.name,Shubham.ID,Shubham.age);
    // Display(Aryan.name,Aryan.ID,Aryan.age);

    // printf("%s %d\n",Shubham.name,Shubham.ID);

    ptr = &Aryan;

    printf("%s %d %d\n",Shubham.name,Shubham.ID,Shubham.age);
    printf("%s %d %d\n",ptr->name,ptr->ID,ptr->age);

    Display(&Aryan);

    printf("\n%d\n%d\n%d",&Shubham+1,&Ashish,&Ankur);
}