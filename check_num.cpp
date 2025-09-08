#include <iostream>
using namespace std;

int check_int(int max) {
    int under = -2147483550;
    int over = 2147483550;

    int j = 0;
    while (j<max) {
        std::cout<<"    Loop: "<<j<<", Under: "<<under<<", Over: "<<over<<std::endl;

        under = under-1;
        over = over+1;
        j = j+1;
    }

    return 0;
}


int check_uint(int max) {
    unsigned int under = 10;
    unsigned int over = 4294967286;

    int j = 0;
    while (j<max) {
        std::cout<<"    Loop: "<<j<<", Under: "<<under<<", Over: "<<over<<std::endl;

        under = under-1;
        over = over+1;
        j = j+1;
    }

    return 0;
}

int check_float(int max) {
    float under = 1.0;
    float over = 1.0;

    int j=0;
    while (j<max) {
        std::cout<<"    Loop: "<<j<<", Under: "<<under<<", Over: "<<over<<std::endl;

        under = under/2;
        over = over*2;
        j = j+1;
    }

    return 0;
}

int check_double(int max) {
    double under = 1.0e-200;
    double over = 1.0e200;

    int j=0;
    while (j<max) {
        std::cout<<"    Loop: "<<j<<", Under: "<<under<<", Over: "<<over<<std::endl;

        under = under/2;
        over = over*2;
        j = j+1;
    }

    return 0;
}

int main() {
    std::cout<<"Hello Wig!"<<std::endl;
    std::cout<<"Check integers:"<<std::endl;
    int ci_int = check_int(200);
    std::cout<<"Check unsigned integers:"<<std::endl;
    int cu_int = check_uint(20);
    std::cout<<"Check floats:"<<std::endl;
    int cf_int = check_float(155);
    std::cout<<"Check doubles:"<<std::endl;
    int cd_int = check_double(450);
    return 0;
}
