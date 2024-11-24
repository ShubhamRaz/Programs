#include <stdio.h>

int main() 
{
    int n;
    scanf("%d", &n);  // Input the size (n)

    // Loop through rows
    for (int i = 0; i < n * 2 - 1; i++) {
        // Loop through columns
        for (int j = 0; j < n * 2 - 1; j++) {
            // Find the minimum distance from the edges (top, bottom, left, right)
            int min = i < j ? i : j; // Min between row and column indices
            min = min < (n * 2 - 2 - i) ? min : (n * 2 - 2 - i); // Compare with distance to bottom
            min = min < (n * 2 - 2 - j) ? min : (n * 2 - 2 - j); // Compare with distance to right
            printf("%d ", n - min); // Print the value based on distance
        }
        printf("\n"); // Move to the next line after printing one row
    }

    return 0;
}
