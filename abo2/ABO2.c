
#include <stdlib.h>
#include  <stdio.h> 
#include "Windows.h"


int main(int argc, char** argv) {

	MessageBoxA((HWND)-0, (LPCSTR) "A ejecutar la calculadora..\n", (LPCSTR)"Vamosss", (UINT)0);
	char buf[1024];

	gets(buf);
	exit(1);
}