#include <stdio.h>
#include <string.h>

void Display(char *s, int id , int age){
    printf("Name: %s\nID: %d\nAge: %d\n",s,id,age);
}

int main(){
    struct Student{
        char name[20];
        int ID;
        int age;
    };


    struct Student Shubham,Ashish,Ankur;

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
    Display(Shubham.name,Shubham.ID,Shubham.age);
    Display(Aryan.name,Aryan.ID,Aryan.age);
}