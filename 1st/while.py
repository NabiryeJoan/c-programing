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



#example 2
# we have a while loop that runs until the number reaches 11.
#  Inside the loop, we use a conditional statement (if-else)
#  to check if the number is even or odd. Based on the result
#include <stdio.h>

int main() {
    int number = 1;

    while (number <= 10) {
        if (number % 2 == 0) {
            printf("%d is even.\n", number);
        } else {
            printf("%d is odd.\n", number);
        }
        
        number++;
    }

    printf("Loop finished.\n");

    return 0;
}
