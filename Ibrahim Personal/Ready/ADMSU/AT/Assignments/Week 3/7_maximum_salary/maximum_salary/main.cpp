#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;
using std::vector;
using std::string;

string largest_number(vector<string> a) {
  //write your code here
  std::stringstream ret;
  string first, second;

    for (size_t i=0; i<a.size()-1; i++) {
        for (size_t j=i+1; j<a.size(); j++) {
            first = a[i] + a[j];
            second = a[j] + a[i];

            if (first < second) {
                string temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

  for (size_t i = 0; i < a.size(); i++) {
    ret << a[i];
  }

  string result;
  ret >> result;
  return result;
}


int main() {
  int n;
  std::cin >> n;
  vector<string> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::cout << largest_number(a);
}
