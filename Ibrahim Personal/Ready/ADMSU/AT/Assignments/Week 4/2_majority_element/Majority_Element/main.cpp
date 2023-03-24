#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;
using namespace std;

vector<int> merge_majority_finder (vector<int> &a, vector<int> &b) {
      int majority_element_a, majority_element_b, majority_element, counter;
      counter = 0;
      majority_element_a = a.back();
      majority_element_b = b.back();
      a.pop_back();
      b.pop_back();

      /*
    cout << "a_merge" << endl;
    for (size_t i=0; i<a.size(); i++) {
      cout << a[i] << " ";
    }
    cout << endl;

    cout << "b_merge" << endl;
    for (size_t i=0; i<b.size(); i++) {
      cout << b[i] << " ";
    }
    cout << endl;

    */



    if ((majority_element_a == majority_element_b) && (majority_element_a != (-1))) {
        a.insert(a.end(), b.begin(), b.end());
        a.push_back(majority_element_a);
        return a;
    }



    else if (majority_element_a == -1 && majority_element_b == -1 && a.size() != 1) {
        a.insert(a.end(), b.begin(), b.end());
        a.push_back(-1);
        return a;
    }



    //else if (majority_element_a == -1 || majority_element_b == -1) {
    else {

            a.insert(a.end(), b.begin(), b.end());
            for(int i=0; i < a.size(); i++) {
                for(int j=0; j < a.size(); j++) {
                       // cout << "a[" << j << "] = " << a[j] << endl;
                    if (a[i] == a[j])
                        counter += 1;

                    if (counter > a.size()/2) {
                        majority_element = a[i];
                        a.push_back(majority_element);
                        return a;
                        }
                }
                counter = 0;
            }
            a.push_back(-1);
            return a;
    }

}




vector<int> majority_element_finder (vector<int> &a) {
  //int majority_element;
  //majority_element = a.back();
  a.pop_back();

  if (a.size() == 1) {
        a.push_back(-1);
        return a;
  }

  //a.push_back(-1);

  //vector <int> a_bar;



  /*
    cout << "Received_array" << endl;
    for (size_t i=0; i<a.size(); i++) {
      cout << a[i] << " ";
    }
    cout << endl;
    */




  int mid = (a.size()/2);
  vector <int> b = vector<int> (a.begin(), a.begin() + mid);
  vector <int> c = vector<int> (a.begin() + mid , a.end());
  b.push_back(-1);
  c.push_back(-1);


  /*
      cout << "b" << endl;
    for (size_t i=0; i<b.size(); i++) {
      cout << b[i] << " ";
    }
    cout << endl;

      cout << "c" << endl;
    for (size_t i=0; i<c.size(); i++) {
      cout << c[i] << " ";
    }
    cout << endl;

    */

  b = majority_element_finder(b);
  c = majority_element_finder(c);

  /*
      cout << "b_bar" << endl;
    for (size_t i=0; i<b_bar.size(); i++) {
      cout << b_bar[i] << " ";
    }
    cout << endl;

      cout << "c_bar" << endl;
    for (size_t i=0; i<c_bar.size(); i++) {
      cout << c_bar[i] << " ";
    }
    cout << endl;

    */
  a = merge_majority_finder(b,c);



  /*
  cout << "a_bar" << endl;
  for (size_t i = 0; i < a_bar.size(); ++i) {
    cout << a_bar[i] << " ";
  }

  cout << endl;
  */

return a;
}

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];

  a.push_back(-1);
  a = majority_element_finder(a);

  /*
  cout << "Result Array" << endl;
  for (size_t i=0; i<a.size(); i++) {
      cout << a[i] << " ";
  }
  cout << endl;
  */

  if (a.back() == -1)
    return 0;
  else
    return 1;

}


int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (get_majority_element(a, 0, a.size())) << '\n';
}

