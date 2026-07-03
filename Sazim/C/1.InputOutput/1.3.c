// 1.3. Write a program that read and display an integer number

#include <stdio.h>

int main()
{
	printf("Please enter an interger number: ");
	int num; // variable declaration
	scanf("%d", &num); // taking intput of the variable
	// & - address of

	printf("Your entered interger value is: %d\n", num);

	return 0;
}