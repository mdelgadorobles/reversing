int main(int argv,char **argc) {
        char *pbuf=malloc(strlen(argc[2])+1);
        char buf[256];

        strcpy(buf,argc[1]);
        for (;*pbuf++=*(argc[2]++););
        exit(1);
}
