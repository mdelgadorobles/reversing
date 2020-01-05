//gcc -m32 -no-pie -fno-stack-protector -ggdb -mpreferred-stack-boundary=2 -z execstack stack01.c

int main(int argv,char **argc) {

	extern system,puts;                           
	void (*fn)(char*)=(void(*)(char*))&system;    /* fn: puntero almacenado en la pila */
	char buf[256];

	fn=(void(*)(char*))&puts;
	strcpy(buf,argc[1]);
	fn(argc[2]);

	exit(1);                                      /* main() no retorna. Salida con error */
}
