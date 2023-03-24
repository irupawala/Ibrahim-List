#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;
using namespace std;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here

    int max_tank, refills;
    max_tank = tank;
    refills = 0;

    //for (size_t i = 0; i <= stops.size(); i++){
    //    cout << "i = " << i << " stops = " << stops[i] << endl;
    //}

    for (int i = 0; i < stops.size(); i++){
         // cout << "i = " << i << " stops = " << stops[i] << " tank_0 = " << tank  << " distance  = " << (stops[i+1] - stops[i]);
        if ((stops[i+1] - stops[i]) <= tank)
            tank -= (stops[i+1] - stops[i]);

        else {
            if ((stops[i+1] - stops[i]) < max_tank) {
                refills += 1;
                tank = max_tank;
                tank -= (stops[i+1] - stops[i]);
                }
            else
                return -1;
        }
        cout << " tank = " << tank << " refills = " << refills << endl;
    }
    return refills;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n+1);
    for (int i = 1; i <= n; ++i)
        cin >> stops[i];

    stops[0] = 0;
    stops[n+1] = d;

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
