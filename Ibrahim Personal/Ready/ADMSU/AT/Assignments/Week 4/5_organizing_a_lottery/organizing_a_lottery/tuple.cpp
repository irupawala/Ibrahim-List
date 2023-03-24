#include <iostream>     // std::cout
#include <algorithm>    // std::transform
#include <vector>       // std::vector
#include <functional>   // std::plus
#include <tuple>

using std::vector;
using namespace std;

int op_increase (int i) { return {i, -1}; }

int main()
{

    /*
    vector<tuple<int, int> > v;
    v.push_back(make_tuple(10, 20));
    v.push_back(make_tuple(15, 5));
    v.push_back(make_tuple(3, 2));

    get<0>(v[0]) = 150;

    // Printing vector tuples
    for (int i = 0; i < v.size(); i++)
        cout << get<0>(v[i]) << " "
             << get<1>(v[i]) << "\n";
    */

    vector<tuple<int, int> > bar;

    vector<int> foo;

    // set some values:
    for (int i=1; i<6; i++)
    foo.push_back (i*10);

    for (int i = 0; i < bar.size(); i++)
    cout << get<0>(bar[i]) << " "
        << get<1>(bar[i]) << "\n";

    bar.resize(foo.size());

    transform (foo.begin(), foo.end(), bar.begin(), op_increase);

    return 0;
}
