#include <iostream>
#include <string>
#include "big_data_int.h"

int main() 
{
    cout<<"please input two numbers:"<<endl;
    string s_a, s_b;
    cin>>s_a;
    cin>>s_b;

    cout<<"Please input the operator(+,-,*,/,%):"<<endl;
    string op;
    cin>>op;

    big_data_int a(s_a), b(s_b), c;

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
            return -1;
    }

    cout <<"Result is:"<<endl<<c.data()<<endl;

    return 0;
}

void test(){}
