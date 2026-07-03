// 1.3. Write a program that read and display an integer number

#include <stdio.h>

int main()
{
	// Disable stdout buffering completely
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Please enter an interger number: ");
	int num; // variable declaration
	scanf("%d", &num); // taking intput of the variable
	// & - address of

	printf("Your entered interger value is: %d\n", num);

	return 0;
}