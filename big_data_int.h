#include <string>
#include <string.h>
using namespace std;

int getValue(int in);

class big_data_int {
    friend big_data_int operator *(const big_data_int &, const big_data_int &);
    friend big_data_int operator /(const big_data_int &, const big_data_int &);
    friend big_data_int operator -(const big_data_int &, const big_data_int &);
    friend big_data_int operator +(const big_data_int &, const big_data_int &);
    friend big_data_int operator %(const big_data_int &, const big_data_int &);
public:
    big_data_int(): _data(""), _len(0) {}
    big_data_int(string _s): _data(_s), _len(_s.length()) {}
    ~big_data_int() {}
    const char* data() const { return _data.c_str();}
    const int length() const {return _len;}
    big_data_int(const big_data_int &d): _data(d._data), _len(d._len) {}
    big_data_int(const big_data_int &a, const big_data_int &b) {
        string s = string(a.data()) + string(b.data());
        _data = s;
        _len = s.length();
    }
    big_data_int & operator = (const big_data_int &d) {
        _data = d._data;
        _len = d._len;

        return *this;
    }

private:
    string _data;
    int _len;
    bool gt(const big_data_int &b) const {
        if(length() == b.length()) {
            return strcmp(data(), b.data()) >= 0;
        }

        return (length() > b.length())? true : false;
    }

    bool is_zero() const {
        const char *p = data();
        const char *q = p + length();
        while (p < q) {
            if (*p++ != '0') {
                return false;
            }
        }
        
        return true;
    }
};


big_data_int  operator *(const big_data_int &, const big_data_int &);
big_data_int  operator /(const big_data_int &, const big_data_int &);
big_data_int  operator -(const big_data_int &, const big_data_int &);
big_data_int  operator +(const big_data_int &, const big_data_int &);

