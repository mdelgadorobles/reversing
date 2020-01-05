#include <stdlib.h>
#include  <stdio.h> 

//gcc -m32 -no-pie -fno-stack-protector -ggdb -mpreferred-stack-boundary=2 -z execstack stack01.c

int main(int argc, char **argv) {

	int cookie;
	char buf[80];

	printf("buf: %08x cookie: %08x\n", &buf, &cookie);
	gets(buf);

	if (cookie == 0x41424344)
		printf("you win!\n");

}
