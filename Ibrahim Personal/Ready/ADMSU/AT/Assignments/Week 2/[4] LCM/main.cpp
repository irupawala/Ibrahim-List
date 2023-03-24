#include <iostream>

using namespace std;

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}


long long lcm (int a, int b) {

    long long first, second, gcd;
    if (a < b) {
        first = b;
        second = a;
    } else {
    first = a;
    second = b;
    }

    while (second > 0) {
            int outcome = first % second;
            first = second;
            second = outcome;
    }

    gcd = first;

   // cout << a << endl;
   // cout << b << endl;
   // cout << gcd << endl;

    first = a;
    second = b/gcd;

    // cout << first << endl;
    // cout << second << endl;

    return (long long) first * second;

}
int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
