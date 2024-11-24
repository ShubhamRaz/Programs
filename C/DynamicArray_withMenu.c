#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
}Dynamic_arr;

void initialize(Dynamic_arr *arr, int Capacity);
void insert(Dynamic_arr *arr,int value);
void delete(Dynamic_arr *arr, int value);
void Display(Dynamic_arr *arr);
void Free(Dynamic_arr *arr);
void deleteALL(Dynamic_arr *arr, int value);

int main()
{
    Dynamic_arr arr;
    initialize(&arr,5);
    int choice, value;

    do {
        printf("\nMenu:\n");
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("22. Delete All\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(&arr, value);
                break;
            case 2:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                delete(&arr, value);
                break;

            case 22:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                deleteALL(&arr, value);
                break;
            case 3:
                Display(&arr);
                break;
            case 4:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 4);

    Free(&arr);
    return 0;
}

void initialize(Dynamic_arr *arr, int Capacity)
{
    arr->data = (int *)malloc(Capacity*sizeof(int));
    arr->size = 0;
    arr->capacity = Capacity;
}

void insert(Dynamic_arr *arr,int value)
{
    if(arr->size == arr-> capacity)
    {
        arr->capacity *=2;
        arr->data = (int *)realloc(arr->data,arr->capacity*sizeof(int));

        if(!arr->data)
        {
            printf("Memory Allocation failed!");
        }
    }

    arr->data[arr->size++]=value;
}

void deleteALL(Dynamic_arr *arr, int value)
{
    int found = 0;
    for(int i = 0; i<arr->size; i++ )
    {
        if(arr->data[i] == value)
        {
            found = 1;
            for(int j = i; j<arr->size-1;j++)
            {
                arr->data[j]=arr->data[j+1];
            }

            i--;
            arr->size--;
        }
        

    }

    if(!found)
    {
        printf("Element not found!");
    }

    else
    {
        printf("All Element %d deleted Successfully\n",value);
    }


}

void delete(Dynamic_arr *arr, int value)
{
    int found = 0;
    for(int i = 0; i<arr->size; i++ )
    {
        if(arr->data[i] == value)
        {
            found = 1;
            for(int j = i; j<arr->size-1;j++)
            {
                arr->data[j]=arr->data[j+1];
            }
            printf("Element %d deleted Successfully\n",value);
            arr->size--;

            break;
        }
        

    }

    if(!found)
    {
        printf("Element not found!");
    }

}
void Display(Dynamic_arr *arr)
{
    if(arr->size == 0)
    {
        printf("Empty Array");
    }

    else
    {
        for(int i = 0;i<arr->size;i++)
        {
            printf("%d ",arr->data[i]);
        }
    }
}

void Free(Dynamic_arr *arr)
{
    free(arr->data);
    arr->size = 0;
    arr->capacity = 0;
}