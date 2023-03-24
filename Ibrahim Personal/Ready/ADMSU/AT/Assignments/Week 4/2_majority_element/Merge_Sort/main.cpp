#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;
using namespace std;

vector<int> Merge (vector<int> &a, vector<int> &b) {
    vector<int> c;

    /*
    cout << "first_array_in_merge" << endl;
    for (size_t i=0; i<a.size(); i++) {
      cout << a[i] << " ";
    }
    cout << endl;

    cout << "second_array_in_merge" << endl;
    for (size_t i=0; i<b.size(); i++) {
      cout << b[i] << " ";
    }
    cout << endl;
    */

    while (a.size() > 0 && b.size() > 0) {

           // cout << "a_size_init = " << a.size() << " b_size_init = " << b.size() << endl;
            if(a[0] <= b[0]) {
                c.push_back(a[0]);
                a.erase(a.begin());
                }
            else {
                c.push_back(b[0]);
                b.erase(b.begin());
                }
           // cout << "c_last_element = " << c.back() << endl;
           // cout << "a_size_fin = " << a.size() << " b_size_fin = " << b.size() << endl;
    }

    if(a.size() != 0) {
    for (size_t i=0; i<a.size(); i++) {
        c.push_back(a[i]);
    }
    }

    if(b.size() != 0) {
    for (size_t i=0; i<b.size(); i++) {
        c.push_back(b[i]);
    }
    }
    /*
    cout << "Result_in_merge" << endl;
    for (size_t i=0; i<c.size(); i++) {
      cout << c[i] << " ";
    }
    cout << endl;
    */

    return c;
}

vector<int> MergeSort(vector<int> &a, int left, int right) {
  if (left == right) return a;
  if (left == right - 1) return a;
  vector <int> a_bar;

  /*
  cout << "Input array" << endl;
  for (size_t i=0; i<a.size(); i++) {
      cout << a[i] << " ";
  }
  cout << endl;
  */

  int mid = (a.size()/2);

  //cout << "left= " << left << " right= " << right << " Mid= " << mid << endl;

  vector <int> b = vector<int> (a.begin(), a.begin() + mid);
  vector <int> c = vector<int> (a.begin() + mid , a.end());

  b = MergeSort(b, 0, b.size());
  c = MergeSort(c, 0, c.size());
  a_bar = Merge(b,c);

 /*
  cout << "Result array" << endl;
    for (size_t i=0; i<b.size(); i++) {
      cout << b[i] << " ";
    }
    cout << endl;
    */

  return a_bar;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }

  vector<int> c;
  c = MergeSort(a, 0, a.size());

  //MergeSort(a, 0, a.size());

 // cout << "Returned Array" << endl;
  for (size_t i = 0; i < c.size(); ++i) {
    cout << c[i] << " ";
  }



}

