#include <stdio.h>

void clearScreen() {
	// The function to clear the screen

	for (int i = 0; i < 500; i++) {
		printf("\e[1;1H\e[2J");
	}
}

int main() {
	int num;
	printf("Enter a number please : ");
	scanf("%d", &num);
	clearScreen();
	printf("The number you entered is %d\n", num);
	return 0;
}
