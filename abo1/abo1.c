#include <stdlib.h>
#include  <stdio.h> 

void f(int nada) {
	char buf[1024];
	gets(buf);
}

int main(int argc, char **argv) {
	f(1);
	printf("hola\n");
}
