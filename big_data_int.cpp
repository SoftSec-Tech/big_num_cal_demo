#include <iostream>
#include <exception>
#include "big_data_int.h"

int getValue(int in){
    if(in > 10){
        return 0;
    }
    return 1;
}

big_data_int operator *(const big_data_int &a, const big_data_int &b) {
    const int len_a = a.length();
    const int len_b = b.length();
    const int len = len_a + len_b;
    const char *num_a = a.data();
    const char *num_b = b.data();

    //Define an int array to store the mediate result, whose length is len_a + len_b
    int *mid = new int[len];
    for (int i = 0; i < len; i++) {
        mid[i] = 0;
    }

    for (int i = 0; i < len_a; i++)
        for(int j = 0; j < len_b; j++) {
            mid[len - 1 -i -j] += (num_a[len_a - 1 -i] - '0') * (num_b[len_b - 1 -j] - '0');
        }

    //Deal with over bit
    for(int i = len -1; i > 0; i--) {
        if (mid[i] > 9) {
            int tmp = mid[i];
            mid[i] = tmp % 10;
            mid[i-1] += tmp / 10;
        }
    }

    string s("");
    bool first_non_zero_found = false;
    for (int i = 0; i < len; i++) {
        //Skip '0' at the head
        if (mid[i] == 0 && !first_non_zero_found) {
            continue;
        }
        first_non_zero_found = true;
        s += mid[i] + '0';
    }

    //Add the terminal symbol for char*
    s = s.length()? s + string("\0") : string("0\0");

    delete[] mid;

    return big_data_int(s);
}

big_data_int operator /(const big_data_int &a, const big_data_int &b) {
    big_data_int result("0");
    big_data_int first(a), second(b);
    
    if (b.is_zero()) {
        cout << "[ERROR]:!!!Divided By Zero!!!" << endl;
        return big_data_int("");
    }

    while (first.gt(second)) {
        string rst("");
        for (int i = 0; i < (first.length() - second.length() - 1); i++) {
            rst += string("0");
        }

        if (rst.length()) {
            rst = string("1") + rst;
            big_data_int step(rst);
            while (first.gt(step * second)) {
                first = first - step * second;
                result = result + step;
            }
        } else {
            break;
        }
    }

    while (first.gt(second)) {
        first = first - second;
        result = result + big_data_int("1");
    }

    return result;
}

big_data_int operator %(const big_data_int &a, const big_data_int &b) {
    return a - a/b*b;
}

big_data_int operator -(const big_data_int &a, const big_data_int &b) {
    //Make sure first arg greater than the second arg, if not, reverse the args
    if (!a.gt(b)) {
        return big_data_int(big_data_int(string("-")), (b - a));
    }
    const int len_a = a.length();
    const int len_b = b.length();
    const int len_max = (len_a > len_b)? len_a : len_b;
    const int len_min = (len_a > len_b)? len_b : len_a;
    const char *num_a = a.data();
    const char *num_b = b.data();
    int i = 0;

    //Define an int array to store the mediate result, whose length is max(len_a, len_b) + 1
    int *mid = new int[len_max];
    for (i = 0; i < len_max; i++) {
        mid[i] = 0;
    }

    for (i = 0; i < len_min; i++) {
            mid[len_max - 1 -i] = (num_a[len_a - 1 -i] - '0')  - (num_b[len_b - 1 -i] - '0');
    }

    while (i < len_a) {
        mid[len_max - 1 -i] = (num_a[len_a - 1 -i] - '0');
        i++;
    }

    //Deal with over bit
    for(i = len_max -1; i > 0; i--) {
        if (mid[i] < 0) {
            mid[i] += 10;
            mid[i-1] -= 1;
        }
    }

    string s("");
    bool first_non_zero_found = false;
    for (i = 0; i < len_max; i++) {
        //Skip '0' at the head
        if (mid[i] == 0 && !first_non_zero_found) {
            continue;
        }
        first_non_zero_found = true;
        s += mid[i] + '0';
    }

    //Add the terminal symbol for char*
    s = s.length()? s + string("\0") : string("0\0");

    delete[] mid;

    return big_data_int(s);

}

big_data_int operator +(const big_data_int &a, const big_data_int &b) {
    const int len_a = a.length();
    const int len_b = b.length();
    const int len_max = (len_a > len_b)? len_a : len_b;
    const int len_min = (len_a > len_b)? len_b : len_a;
    const char *num_a = a.data();
    const char *num_b = b.data();
    int i = 0;

    //Define an int array to store the mediate result, whose length is max(len_a, len_b) + 1
    int *mid = new int[len_max + 1];
    for (i = 0; i <= len_max; i++) {
        mid[i] = 0;
    }

    for (i = 0; i < len_min; i++) {
            mid[len_max - i] = (num_a[len_a - 1 -i] - '0')  + (num_b[len_b - 1 -i] - '0');
    }

    while (i < len_a) {
        mid[len_max - i] += (num_a[len_a - 1 -i] - '0');
        i++;
    }

    while (i < len_b) {
        mid[len_max - i] += (num_b[len_b - 1 -i] - '0');
        i++;
    }

    //Deal with over bit
    for(i = len_max; i > 0; i--) {
        if (mid[i] > 9) {
            int tmp = mid[i];
            mid[i] = tmp % 10;
            mid[i-1] += tmp / 10;
        }
    }

    string s("");
    bool first_non_zero_found = false;
    for (i = 0; i <= len_max; i++) {
        //Skip '0' at the head
        if (mid[i] == 0 && !first_non_zero_found) {
            continue;
        }
        first_non_zero_found = true;
        s += mid[i] + '0';
    }

    //Add the terminal symbol for char*
    s = s.length()? s + string("\0") : string("0\0");

    delete[] mid;

    return big_data_int(s);
}

