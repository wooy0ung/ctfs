#include <stdio.h>

char str[] = "000000000000000000000000000000000000000000000000000101110000110001000000101000000001";

int main()
{
	int cnt = 0;
	while(str[cnt] != '\0')
		cnt++;
	printf("[ %d char ]", cnt);

	return 0;
}