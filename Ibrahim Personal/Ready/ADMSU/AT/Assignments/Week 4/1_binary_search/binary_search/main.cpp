#include <iostream>
#include <cassert>
#include <vector>
#include <cmath>
#include <cstdlib>

using std::vector;
using namespace std;

//int binary_search(const vector<int> &a, int x) {
int binary_search(vector<int> &a, int x) {
  int low = 0, high = (int)a.size()-1;
  //int mid = floor((low + (high - low)/ 2));
  //cout << "low_Init = " << low << " high_Init = " << high << " mid_Init = " << mid  << " x_init = "<< x << " a[mid]_init = " << a[mid] << endl;

  while (low <= high) {


  int mid = floor((low + (high - low)/ 2));
  //cout << "low = " << low << " high = " << high << " mid = " << mid  << " x = "<< x << " a[mid] = " << a[mid] << endl;

  if (a[mid] == x)
    return mid;

  else if (x < a[mid])
    high = mid - 1;

  else if (x > a[mid])
    low = mid + 1;

  }

  return -1;

}

int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {

/*
     while (true) {

        int n = rand() % 10;
        cout << n << endl;
        vector<int> a(n);
        for (size_t i = 0; i < a.size(); i++) {
                a[i] = rand() % 100;
        }

        for (size_t i = 0; i < a.size(); i++) {
                cout << a[i] << ' ';
        }
        cout << endl;

        int m = rand() % 10;
        cout << m << endl;
        vector<int> b(m);
        for (size_t i = 0; i < b.size(); i++) {
                b[i] = rand() % 100;
        }

        for (size_t i = 0; i < b.size(); i++) {
                cout << b[i] << ' ';
        }
        cout << endl;

        for (int i = 0; i < m; ++i) {
        int res1 = linear_search(a, b[i]);
        int res2 = binary_search(a, b[i]);


        if (res1 != res2) {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else {
            cout << "OK" << endl;
        }

        }
    }

*/


  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }


  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    //std::cout << linear_search(a, b[i]) << ' ';
    std::cout << binary_search(a, b[i]) << ' ';
    //std::cout << binary_search(a, b[i]) << endl;
  }

  //cout << "Returned_Value" << binary_search(a, b[0]) << endl;


}
