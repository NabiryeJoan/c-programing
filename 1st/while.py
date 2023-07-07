#include <stdio.h>
#while loop

int main() {
    int input;
    printf("Enter a number (-1 to exit): ");
    scanf("%d", &input);

    while (input != -1) {
# Perform some operations based on the input
        printf("You entered: %d\n", input);

        #Prompt for the next input
        printf("Enter a number (-1 to exit): ");
        scanf("%d", &input);
    }

    printf("Program exited.\n");

    return 0;
}
