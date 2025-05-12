#include<stdio.h> 

int main(int argc, char** argv) {
    long i = 0;
    long s = 0;
    for (; i < 1000; i++) {
    //for (; i < 1000000000; i++) {
        s += i;
    }
    printf("%ld\n", s);
    return 0;
}
