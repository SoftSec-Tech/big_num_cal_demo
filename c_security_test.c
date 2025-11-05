
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_BUFFER 10

void buffer_overflow_vuln(char* user_input) {
    char buffer[MAX_BUFFER]; // 10 bytes buffer
    strcpy(buffer, user_input); 
    printf("Copied to buffer: %s\n", buffer);
}


int integer_overflow_vuln(int count, int size) {
    int total_bytes = count * size; 
    return total_bytes;
}


int main(int argc, char* argv[]) {
    buffer_overflow_vuln(argv[1]);
    int result = integer_overflow_vuln(INT_MAX, 2);
    return 0;
}