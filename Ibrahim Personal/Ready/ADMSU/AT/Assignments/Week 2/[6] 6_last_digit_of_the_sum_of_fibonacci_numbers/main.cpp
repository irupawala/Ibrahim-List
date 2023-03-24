#include <iostream>

using namespace std;

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

long long  get_fibonacci_partial_sum (long long n) {
    long long duration = n %60; // 60 because last digit repeats after 60
    if (duration <= 1)
        return duration;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;




    for (long long i = 2; i <=duration ; i++) { // now taking the sum of the last digits of the numbers till the duration that is nth number in a sequence of 60 digits
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous%10 + previous%10;
        sum += current;
        //int x = sum%10 ;

       // cout << "x" << i << " = " << x << endl;
    }

    return sum % 10;
}


int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_naive(n) << endl;
    std::cout << get_fibonacci_partial_sum(n) << endl;
}
