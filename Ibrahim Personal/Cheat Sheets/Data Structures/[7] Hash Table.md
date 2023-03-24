# Hash Table

* **Direct Addressing**: Integer array of size n. Access time and update time is O(1). Biggest Disadvantage is Memory consumption is O(n).
* **List Based Mapping**: Store only active data in the list (Linked List). Memory consumption is θ(n). Append, Access, Top and Pop are θ(1). Disadvantage now is that Find and Erase are θ(n).
* **Hash Function**: For any set of objects S and any integer m > 0, a function h: S --> {0, 1, .., m-1} is called a hash function. m is called the cardinality of hash function h.
* **Collision**: When h(o1) = h(o2) & o1 != o2 then, it is collision.
* **Chaining Approach**: 
  * In the chaining approach, hash table is an array of linked lists. i.e. each index has its own linked list.
  * All key-value pairs mapping to the same index will be stored in the linked list of that index.
  * Let c be the length of the longest chain in A. Then the running time of HasKey, Get and Set is **θ(c+1)**
  * Let n be the number of different keys O currently in the map and m be the cardinality
    of the hash function. **Then the memory consumption for chaining is θ(n+m)**.
  * α = n/m is called **load factor**
  * **Both small m and c is required for better time complexity.**
  * Implementation of set and map using chaining is called a hash table.
  * Set is set() and Map is dict() in python.

![1643168563611](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1643168563611.png)

* Universal Family – Let U be the universe – the set of all possible keys. A set of hash
  function is called universal family if for any two keys x, y Є U, x != y the probability of collision is <= 1/m.
* If h is chosen randomly from a universal family, the average length of the longest chain c is O(1 + α).
* Ideally load factor 0.5 < α < 1.
* Use O(m) = O(n/α) = o(n) memory to store n keys.
* Use dynamic has tables, rehash when load factor > 0.9. Single rehashing takes O(n) time, but amortized running time of each operation with hash table is still O(1) on average.

* **Hashing Strings and Hashing Integers**

## **Time for common operations**

* Amortized run time is O(1 + α). however it suffers from `O(n)` **worst case** time complexity due to two reasons:
  * If too many elements were hashed into the same key: looking inside this key may take O(n) time.	
  * Once a hash table has passed its load balance - it has to rehash

## When to Use ?

* Use it when a key is to be associated to a value. 

## Python Implementation

* Dictionary is the python's implementation of the hash table.
* In Dictionary, the key must be unique and immutable. This means that a **Python Tuple** can be a key whereas a **Python List** can not.

```python
price_lookup = {'apples': 2.99, 'oranges':3.45, 'kiwi':2.89}
d = {'key1':{'nestkey':{'subnestkey':'value'}}} # Dictionary nested inside a dictionary nested inside a dictionary
d.keys() # Method to return a list of all keys 
d.values() # Method to grab all values
d.items() # Method to return tuples of all items  (we'll learn about tuples soon)
d['key2'] = 'Jebaaaaa'
d['key2'] = "Dangal" # you can also modify values but not keys
for k,v in d.items(): print (k,v) # Keys and values can be accessed using items 
{k:v**2 for k,v in zip(['a', 'b', 'c', 'd'], range(4))}
dict = {k:v**2 for k,v in zip(['a', 'b', 'c', 'd'], range(4))} # dictionary comprehension
```

### Python Code to understand the implementation of Hash Table (Hashing Integers)

```python
# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count): # here bucket_count is the cardinality factor
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems = []
        self.key = 0
        self.hashTable = [[] for _ in range(bucket_count)]
        

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems) if self._hash_func(cur) == query.ind)
            self.write_chain(cur for cur in reversed(self.hashTable[query.ind]))
        else:
            self.key = self._hash_func(query.s)
            try:
                #ind = self.elems.index(query.s)
                ind = self.hashTable[self.key].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                   #self.elems.append(query.s)
                   self.hashTable[self.key].append(query.s)
            else:
                if ind != -1:
                    #self.elems.pop(ind)
                    self.hashTable[self.key].pop(ind)
        
        #print(self.hashTable)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)  # here bucket_count is the cardinality factor
    proc.process_queries()
```

### DefaultDict

* **Defaultdict** is a container like [dictionaries](https://www.geeksforgeeks.org/python-dictionary/) present in the module **collections**. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

```python
Syntax: defaultdict(default_factory)
Parameters:  

default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
```

```python
# Python program to demonstrate
# defaultdict


from collections import defaultdict


# Function to return a default
# values for keys that is not
# present
def def_value():
	return "Not Present"
	
# Defining the dict
d = defaultdict(def_value)
# d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
```

* **__missing__():** This function is used to provide the default value for the dictionary. This function takes default_factory as an argument and if this argument is None, a KeyError is raised otherwise it provides a default value for the given key. 

```python 
# Python program to demonstrate
# defaultdict


from collections import defaultdict

	
# Defining the dict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
```

* **Using List as default_factory**
* When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.

```python 
# Python program to demonstrate
# defaultdict

from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
	d[i].append(i)
	
print("Dictionary with values as list:")
print(d)
```

* **Using int as default_factory**
* When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.

```python
# Python program to demonstrate
# defaultdict

from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
	
	# The default value is 0
	# so there is no need to
	# enter the key first
	d[i] += 1
	
print(d)
```

* **Follow this link for more**

  https://www.geeksforgeeks.org/defaultdict-in-python/

