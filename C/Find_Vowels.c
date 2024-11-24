#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to check if a character is a consonant
int is_consonant(char c) {
    c = tolower(c);  // Convert to lowercase for uniformity
    return isalpha(c) && !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

// Function to check if a character is a vowel
int is_vowel(char c) {
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main() {
    char a[] = "aeHeoullooosjgaa"; // Input string
    int length = strlen(a);
    int inside_sequence = 0; // Flag to track if we are inside a vowel sequence

    for (int i = 1; i < length - 1; i++) { // Start from 1 and end at length - 1 to avoid boundary issues
        // If the current character is a vowel and is surrounded by consonants
        if (is_vowel(a[i]) && is_consonant(a[i - 1]) && is_consonant(a[i + 1])) {
            if (!inside_sequence) {
                // This means we're starting a new sequence, print a new line if we haven't printed anything yet
                if (i > 1 && inside_sequence == 0) {
                    printf("\n");
                }
                inside_sequence = 1; // Mark that we are inside a sequence
            }
            printf("%c", a[i]); // Print the vowel
        } else if (!is_vowel(a[i]) && inside_sequence) {
            // If we were inside a vowel sequence and hit a consonant, we end the sequence
            inside_sequence = 0; // Reset the flag
            printf("\n"); // Print newline to separate sequences
        }
    }

    return 0;
}
