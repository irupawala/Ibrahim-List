#include <iostream>
using namespace std;

int main()
{
 int n;

 cout <<"Enter no of elements" << endl;
 cin >> n;
 int A[n];

 cout <<"Enter elements" << endl;

 for (int i=0; i<n; i++)
    cin >> A[i];

  for(int j=0; j<n; j++)
    cout << A[j] << " " ;

 return 0;
}
