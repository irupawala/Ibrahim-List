#include <iostream>

using namespace std;

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}


int gcd (int a, int b) {

    long long first, second;
    if (a < b) {
        first = b;
        second = a;
    } else {
    first = a;
    second = b;
    }

    //cout << first << endl;
    //cout << second << endl;

    while (second > 0) {
            int outcome = first % second;
            first = second;
            second = outcome;
    }

    return first;
}
int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
