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





# 2. Stringstream

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



