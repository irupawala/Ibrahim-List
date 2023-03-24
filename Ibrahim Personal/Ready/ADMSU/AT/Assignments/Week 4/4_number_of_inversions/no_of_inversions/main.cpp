#include <iostream>
#include <vector>

using std::vector;
using namespace std;


vector<int> inversion_counter (vector<int> &a, vector<int> &b) {
      int inversion_counter_a, inversion_counter_b, inversion_counter;
      inversion_counter_a = a.back();
      inversion_counter_b = b.back();


      inversion_counter = inversion_counter_a + inversion_counter_b;
      a.pop_back();
      b.pop_back();

     // cout << "Inversion_Counter 1 =============================== " << inversion_counter << endl;


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

    for (size_t i=0; i<a.size(); i++) {
        for (size_t j=0; j<b.size(); j++) {
               // cout << "a[" << i << "] = " << a[i] << endl;
               // cout << "b[" << j << "] = " << b[j] << endl;

            if (a[i] > b[j]) {
               // cout << "a[" << i << "] ========= " << a[i] << endl;
               // cout << "b[" << j << "] ========= " << b[j] << endl;
                inversion_counter+=1;
            }
        }
    }



   // cout << "Inversion_Counter 2 =============================== " << inversion_counter << endl;


    a.insert(a.end(), b.begin(), b.end());
    a.push_back(inversion_counter);
    return a;
}



vector<int> inversion_finder (vector<int> &a) {
  int count;
  count = a.back();
  a.pop_back();

  if (a.size() == 1) {
        a.push_back(0);
        return a;
  }

  //a.push_back(-1);

  vector <int> a_bar;



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
  b.push_back(0);
  c.push_back(0);


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

    vector <int> b_bar, c_bar;


  b_bar = inversion_finder(b);
  c_bar = inversion_finder(c);

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
  a_bar = inversion_counter(b_bar,c_bar);


  /*
  cout << "Returned Array" << endl;

  cout << "a_bar" << endl;
  for (size_t i = 0; i < a_bar.size(); ++i) {
    cout << a_bar[i] << " ";
  }

  cout << endl;
  */



return a_bar;
}




long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right) {
  long long number_of_inversions = 0;
  if (right <= left + 1) return number_of_inversions;
  //size_t ave = left + (right - left) / 2;
  //number_of_inversions += get_number_of_inversions(a, b, left, ave);
  //number_of_inversions += get_number_of_inversions(a, b, ave, right);


  //write your code here
  a.push_back(0);
  a = inversion_finder(a);

  number_of_inversions = a.back();
  return number_of_inversions;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  vector<int> b(a.size());

  //n = get_number_of_inversions(a, b, 0, a.size());
  //cout << "FINAL ANSWER = " << n << endl;
  std::cout << get_number_of_inversions(a, b, 0, a.size()) << '\n';
}
