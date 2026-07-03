// 1.2. An integer variable n contains 5. Write a program that prints value of n.

#include <stdio.h>

int main()
{
	int n = 5; // value initialization (when variable declared and assign to a value at the same time)

	printf("n contains - %d\n", n);

	return 0;
}

/*
	C has four data types

	1. Int
	2. Float
	3. Double
	4. Char

	Format specifier

	Int - %d - 2 byte
	Long Int - %ld - 4 byte
	Long Long Int - %lld - 8 byte

	Float - %f - 4 byte
	Double - %lf - 8 byte
	Char - %c - 1 byte
*/