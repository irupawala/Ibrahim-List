# Cpp Important Syntax Used 

## 1. Vectors

* Same as that of array but no need to mention the size and also initial values for all the elements is zero.
* Syntax 

```cpp
#include <vector>
vector<int> values(n)
```

* Size of Vector

```cpp
values.size()
```

* Passing vector in function by reference

```cpp
int name(int cap, vector <int> &value)
```

* To push and pop elements from vector

```cpp
summands.push_back(i);
summands.pop_back();
```

* To access last element of vector 

```cpp
a.back();
```

* To access first element of vector

```cpp
a.begin();
```

## 2. Stringstream

The class template `std::basic_stringstream` implements input and output operations on string based streams. It effectively stores an instance of [std::basic_string](https://en.cppreference.com/w/cpp/string/basic_string) and performs the input and output operations on it.

Consider this example. Here each string element from a vector is pushed to a single stringstream.

```cpp
#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

string largest_number(vector<string> a) {
  //write your code here
  std::stringstream ret;
  string first, second;

    for (size_t i=0; i<a.size()-1; i++) {
        for (size_t j=i+1; j<a.size(); j++) {
            first = a[i] + a[j];
            second = a[j] + a[i];

            if (first < second) {
                string temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

  for (size_t i = 0; i < a.size(); i++) {
    ret << a[i];
  }

  string result;
  ret >> result;
  return result;
}
```



## 3. Using minHeap and maxHeap

https://www.mygreatlearning.com/blog/priority-queue-in-cpp/

**maxHeap**

```cpp
priority_queue<int> variableName;   // By default, C++ creates a max-heap for the priority queue.
```

**minHeap**

```c++
priority_queue <int, vector<int>, greater<int>> q; 
```

**Some Useful Methods**

q.push()

q.pop()

q.empty()

q.size()

q.top()

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <list>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int i=0; i<nums.size(); i++) {
            if (minHeap.size() < k) {
                minHeap.push(nums[i]);
            }
            else if (nums[i] > minHeap.top()){
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }

        return minHeap.top();
    }
};

int main()
{

    Solution S;
    vector<int> nums_1 = {3,2,1,5,6,4};
    cout << "First Input " << S.findKthLargest(nums_1, 2) << endl;

    vector<int> nums_2 = {3,2,3,1,2,4,5,5,6, 7, 8, 9};
    cout << "Second Input " << S.findKthLargest(nums_2, 4) << endl;    
}
```

## 4. Hash Table - unordered_map (Python Dictionary)

`unordered_map` is a C++ Standard Template Library (STL) container class that provides a hash table data structure for storing key-value pairs. It is similar to `map`, which also stores key-value pairs, but `unordered_map` uses a hash function to map the keys to their corresponding values, which makes lookups faster than in `map`.

Here are some features of `unordered_map`:

- Stores key-value pairs where each key must be unique.
- Provides constant time complexity O(1) for insertion, deletion, and search operations in the average case.
- Allows iteration over the elements in the container using iterators.
- Automatically resizes the container to maintain an optimal load factor (i.e., the ratio of the number of stored elements to the size of the container).
- Uses a hash function to map the keys to their corresponding values, which can be provided as a template parameter or generated by the container.
- The elements in the container are unordered, which means they are not stored in any particular order.

Here's an example of how to use `unordered_map` to store and access key-value pairs:

```c++
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    // Create an unordered_map of strings to ints
    unordered_map<string, int> myMap;

    // Insert some key-value pairs
    myMap.insert({"apple", 1});
    myMap.insert({"banana", 2});
    myMap.insert({"orange", 3});

    // Access the value associated with a key
    cout << "The value of banana is " << myMap["banana"] << endl;

    // Update the value associated with a key
    myMap["apple"] = 4;

    // Iterate over the elements in the container
    for (auto it = myMap.begin(); it != myMap.end(); ++it) {
        cout << it->first << ": " << it->second << endl;
    }

    return 0;
}
```

**find(), end() and it operator**

```c++
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<string, int> myMap;
    myMap["apple"] = 1;
    myMap["banana"] = 2;
    myMap["orange"] = 3;

    cout << "The value of apple is " << myMap["apple"] << endl;
    cout << "The value of banana is " << myMap["banana"] << endl;
    cout << "The value of orange is " << myMap["orange"] << endl;

    if (myMap.find("apple") != myMap.end()) {
        cout << "apple is in the map" << endl;
    }

    if (myMap.find("pear") == myMap.end()) {
        cout << "pear is not in the map" << endl;
    }

    return 0;
}
```

**count() Operator** - `map.count(key)` returns the number of elements in the map container that have a key equivalent to `key`. If the key is found, `count()` returns `1`, otherwise, it returns `0`.

```c++
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement)) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = solution.twoSum(nums, target);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
```
