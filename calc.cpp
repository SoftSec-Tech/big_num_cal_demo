#include "calc.h"

big_data_int calc(big_data_int a, big_data_int b, string op) {
    switch (op.c_str()[0]) {
        case '+':
            c = a + b;
            break;
        case '-':
            c = a - b;
            break;
        case '*':
            c = a * b;
            break;
        case '/':
            c = a / b;
            break;
        case '%':
            c = a % b;
            break;
        default:
            cout<<"Wrong operator input"<<endl;  
            return big_data_int("-1");
    }
    return c;
}