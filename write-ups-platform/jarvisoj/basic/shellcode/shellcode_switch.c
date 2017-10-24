#include <stdio.h>

char source[]="50594949 49494949 4949...";
char shellcode[]=" ";

int main()
{
	printf("[source:]\n%s\n\n", source);

	int i = 0, j = 0;
	while(source[i] != '\0')
	{
		if(source[i] == ' ')
		{
			i++;
			continue;
		}
		shellcode[j++] = '\\';
		shellcode[j++] = 'x';
		shellcode[j++] = source[i++];
		shellcode[j++] = source[i++];
	}

	printf("[shellcode:]\n%s\n\n", shellcode);
	
	return 0;
}