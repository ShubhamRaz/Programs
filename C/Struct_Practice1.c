#include <stdio.h>
#include <string.h>

struct Student{
    int ID;
    char Name[20];
    int Age;
};

typedef struct Student Std;

void Display(Std *b){
    printf("ID: %d\nName: %s\nAge: %d\n\n",b->ID,b->Name,b->Age);
}

int main(){

    Std A1,A2;

    A1.ID = 1;
    strcpy(A1.Name,"Pankaj Kumar");
    A1.Age = 5;

    A2.ID = 2;
    strcpy(A2.Name,"Ashish Kumar");
    A2.Age = 16;  

    Display(&A1);
    Display(&A2);

    printf("%d\n",A2.Age);
    printf("%d\n",A1.Age);

}