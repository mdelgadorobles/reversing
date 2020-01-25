//gcc -m32 -no-pie -fno-stack-protector -ggdb -mpreferred-stack-boundary=2 -z execstack

extern system,puts; 
void (*fn)(char*)=(void(*)(char*))&system;
   
int main(int argv,char **argc) {
	char *pbuf=malloc(strlen(argc[2])+1);
	char buf[256];

	fn=(void(*)(char*))&puts;
	strcpy(buf,argc[1]);		
	strcpy(pbuf,argc[2]);
	fn(argc[3]);
   	
   while(1);
}
