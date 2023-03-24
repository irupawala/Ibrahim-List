#include <iostream>
// Use the link https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836
using namespace std;

long long pisano_length(long long m) {
    long long first = 0, second = 1, current = first + second;
    for (int i = 0; i < m * m; i++) { // m^2 because gives the safest range to encounter 01
        current = (first + second) % m;
        first = second;
        second = current;
        if (first == 0 && second == 1) return i + 1;
    }
}

long long get_fibonacci_huge(long long n, long long m) {

   // cout << "pisano = " << get_pisano_period(m) << endl;
    long long remainder = n % pisano_length(m);
   // cout << "remainder = " << remainder << endl;

    long long first = 0, second = 1, result;

    result = remainder;

    for (int i = 2; i <= remainder; i++) {
        result = (first + second) % m;
            //cout << "iteration = " << i << endl;
            //cout << "res_loop = " << result << endl;
            //cout << "first = " << first << endl;
            //cout << "second = " << second << endl;
        first = second;
        second = result;

    }

    return result % m;
}

int main() {
//    for (int i = 2; i < 100; i++) {
//        std::cout << i << " : " << get_pisano_period(i) << std::endl;
//    }
//    return 0;
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge(n, m) << '\n';
}
