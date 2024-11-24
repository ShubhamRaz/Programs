#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle {
    int a;
    int b;
    int c;
};

typedef struct triangle triangle;

// Function to calculate the area using Heron's formula
double calculate_area(triangle tr) {
    double p = (tr.a + tr.b + tr.c) / 2.0;
    return sqrt(p * (p - tr.a) * (p - tr.b) * (p - tr.c));
}

void sort_by_area(triangle* tr, int n) {
    // Simple bubble sort based on the area
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (calculate_area(tr[j]) > calculate_area(tr[j + 1])) {
                // Swap the triangles if the current one has a larger area than the next
                triangle temp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    triangle *tr = malloc(n * sizeof(triangle));
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &tr[i].a, &tr[i].b, &tr[i].c);
    }

    sort_by_area(tr, n);

    for (int i = 0; i < n; i++) {
        printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
    }
    
    free(tr); // Free the allocated memory
    return 0;
}
