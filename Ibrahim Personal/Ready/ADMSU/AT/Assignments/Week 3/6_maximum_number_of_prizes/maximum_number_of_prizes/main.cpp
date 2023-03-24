#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::max;
using std::vector;
using namespace std;

vector<int> optimal_summands(int n) {
  vector<int> summands;

  long long sum = 0;
  int i, last_digit;

// Generating a vector where each digit is the sum of all the preceeding digits till the element is obtained which is greater then n
  for( i=1; i<=n; i++) {
        sum = sum + i;
        summands.push_back(i);

        if (sum >= n)
            break;
  }


// Last element in the question will be summands[i-2] + summands[i-1] hence removing last two elements and replacing it by this sum
  if (sum > n) {
 // cout << "summands[i] = " << summands[i] << endl;
  //cout << "summands[i-1] = " << summands[i-1] << endl;
  //cout << "summands[i-2] = " << summands[i-2] << endl;

  last_digit = n - (sum - (summands[i-2] + summands[i-1])); // n - sum of digits upto n not including last two digits
  summands[i-2] = last_digit;
  //summands.erase(summands.size());
  summands.pop_back();

  //cout << "sum = " << sum << endl;
  //cout << "i = " << i << endl;
  }

  if (sum = n) {

  }

  return summands;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
}
