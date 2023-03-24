#include <iostream>
#include <stdlib.h>

using namespace std;
int fibonacci_sum_squares_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current * current;
    }

    return sum % 10;
}

long long  fibonacci_sum_squares (long long n) {
    long long duration = n %60;
    if (duration <= 1)
        return duration;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;
    long long square_current;

    for (long long i = 2; i <=duration ; i++) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous%10 + previous%10;
        square_current = (current%10) * (current%10);
        sum += square_current%10;

        //cout << "x" << i << " = " << current%10 << endl;
        //cout << "x*x" << i << " = " << square_current%10 << endl;
        //cout << "sum" << i << " = " << sum%10 << endl;
    }

    return sum % 10;
}

int stress_test() {

    while (true) {
        int rand_1 = rand() % 40;
        cout << "rand_1 = " << rand_1 << endl;

        long long res1 = fibonacci_sum_squares_naive(rand_1);
        long long res2 = fibonacci_sum_squares(rand_1);

        if (res1 != res2) {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else {
            cout << "OK" << endl;
        }
    }
}

int main() {
    long long n = 0;
    std::cin >> n;
    //std::cout << fibonacci_sum_squares_naive(n) << endl;
    std::cout << fibonacci_sum_squares(n) << endl;
    //stress_test();
}
