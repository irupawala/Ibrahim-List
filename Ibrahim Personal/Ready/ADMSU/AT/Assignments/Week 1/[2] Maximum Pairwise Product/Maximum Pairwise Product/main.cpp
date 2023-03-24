#include <iostream>
#include <cstdlib>

using namespace std;

long long MaxPairwiseProduct(int arr[], int num) {

    int i, j, temp;

    long long result;

    for(i=0; i<2; i++) {
        for (j=i+1; j<num; j++) {
            if(arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    result = (long long)arr[0] * (long long)arr[1];
    return (result);
}

long long MaxPairwiseProductCoursera(int arr[], int num) {

    long long result = 0;
    for (int i=0; i<num; i++) {
        for (int j=i+1; j<num; j++) {
            if((long long)arr[i] * (long long)arr[j] > result) {
                result = (long long)arr[i] * (long long)arr[j];
            }
        }
    }

    return result ;
}



int main()
{
  /*  while (true) {
        int num = rand() % 1000 + 2;
        cout << num << endl;
        int arr[num];
        for (int i=0; i<num; i++) {
            arr[i] =  (rand() % 100000);
        }
        for (int i=0; i<num; i++) {
            cout << arr[i] << ' ';
        }
        cout << endl;

        long long res1 = MaxPairwiseProduct(arr, num);
        long long res2 = MaxPairwiseProductCoursera(arr, num);

        if (res1 != res2) {
            cout << "Wrong answer: " << res1 << ' ' << res2 << endl;
            break;
        }
        else {
            cout << "OK" << endl;
        }
    } */

    int num, i;
    long long result;

    cin >> num;
	int arr[num];

    for(i=0; i < num; i++) {
        cin >> arr[i];
    }
    result = MaxPairwiseProduct(arr, num);
    cout << result << endl;
    return 0;

}
