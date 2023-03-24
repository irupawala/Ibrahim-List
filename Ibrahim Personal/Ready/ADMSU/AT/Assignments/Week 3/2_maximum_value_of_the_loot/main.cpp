#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using namespace std;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;


// Linear sorting of maximum value per unit weight. Time - O(n^2)
	for (int i = 0; i<values.size()-1; i++)
	for (int j = i+1; j<values.size(); j++) {
	if ((float) values[i]/weights[i] < (float) values[j]/weights[j]) {
		int temp_values = values[i];
		values[i] = values[j];
		values[j] = temp_values;
		int temp_weights = weights[i];
		weights[i] = weights[j];
		weights[j] = temp_weights;
	}
	}

  /*
  cout << "Sorted_values" << endl;
  for(int i=0; i<values.size(); i++)
    cout << values[i] << endl;

  cout << "Sorted_weights" << endl;
  for(int i=0; i<weights.size(); i++)
    cout << weights[i] << endl;
    
  cout << "CAPACITY=" << capacity << endl;
  cout << "ValueSize" << values.size() << endl;
  */
  
// Filling the Capacity to the max. Time - O(n)  
	for (int i=0; i<values.size(); i++) {

		if (capacity == 0)
				break;

		// if weight is less then capacity take the entire item
		if(capacity > weights[i]) {
			value += values[i];
			capacity -= weights[i];
		}

		else {
				value = (value +   ((double)values[i]/ (double)weights[i]) * capacity);
				capacity -= capacity;
		}
	}


// Total time - O(n^2) + O(n) = O(n^2)
	return value;

}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
        std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(9);
  std::cout << optimal_value << std::endl;
  return 0;
}
