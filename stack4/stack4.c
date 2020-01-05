#include <stdio.h> 

//gcc -m32 -no-pie -fno-stack-protector -ggdb -mpreferred-stack-boundary=2 -z execstack

int main(int argc, char **argv) {
	int cookie;
	char buf[80];

	printf("buf: %08x cookie: %08x\n", &buf, &cookie);
	gets(buf);

	if (cookie == 0x000d0a00)
		printf("you win!\n");

}
