#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;
using namespace std;

int partition2(vector<int> &a, int l, int r) {

{
    cout << "Input Array" << endl;
    for(int i=0; i<a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
}

  int x = a[l];
  int j = l;

  {
    cout << "Initial Values" << endl;
    cout << "x = " << x << " j = " << j << " l = " << l << " r = " << r << endl;
  }

  for (int i = l + 1; i <= r; i++) {
        {
            cout << "Input For loop" << endl;
            cout << "i = " << i << " a[i] = " << a[i] << " j = " << j << " a[j] = " << a[j] << " x = " << x << endl;
        }

    if (a[i] <= x) {
        {
            cout << "Inside If statement" << endl;
            cout << "i = " << i << " a[i] = " << a[i] << " j = " << j << " a[j] = " << a[j] << " x = " << x << endl;
        }

      j++;
      swap(a[i], a[j]);


        {
            cout << "End of If statement" << endl;
            cout << "i = " << i << " a[i] = " << a[i] << " j = " << j << " a[j] = " << a[j] << " x = " << x << endl;
        }
    }

    {
    cout << "End of For Loop Array" << endl;
    for(int i=0; i<a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
    }


  }
  swap(a[l], a[j]);

{
    cout << "Output Array" << endl;
    for(int i=0; i<a.size(); i++)
        cout << a[i] << " ";
    cout << endl;
}

  return j;
}

void randomized_quick_sort(vector<int> &a, int l, int r) {

  {
      cout << "Input l/r Values =============================" << endl;
      cout << " l = " << l << " r = " << r << endl;

  }


  if (l >= r) {
    return;
  }



  int k = l + rand() % (r - l + 1);

  cout << "k ============================ " << k << endl;
  swap(a[l], a[k]);

  int m = partition2(a, l, r);

  {
      cout << "Returned Values =============================" << endl;
      cout << " m = " << m << endl;

  }

  {
      cout << "First Partition" << endl;
  }
  randomized_quick_sort(a, l, m - 1);

    {
      cout << "Second Partition" << endl;

  }
  randomized_quick_sort(a, m + 1, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
}
