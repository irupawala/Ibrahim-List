# Sets

* Sets is UNORDERED collections of "unique" elements. Hence, In a nutshell there can be only one representative of the same object.



```python
s = set()
# add()
s.add(1) # adds element to the set
s.add(2)
print(s)

# clear()
s.clear() # removes all elements from the set
print(s)

s = {1,2,3} # Notice that set is also defined using curly braces like the dictionary
# copy()
sc = s.copy() #makes a copy hence chnages to the original don't affect the copy
print(sc) 

# discard
s.discard(2) # Removes an element from a set if it is a member. If the element is not a member, do nothing.

# intersection 
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2)
print(s1) 

# isdisjoint
# This method will return True if two sets have a null intersection.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2)
s2.isdisjoint(s3)

# union 
# Returns the union of two sets (i.e. all elements that are in either set.)
s1.union(s2)
print(s1)

# issubset
# This method reports whether another set contains this set.
s1 = {1,2}
s2 = {1,2,4}
print(s1.issubset(s2))
```

```python 
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```



# Tuples

* In Python tuples are very similar to lists, however, unlike lists they are *immutable* meaning they can not be changed. 

```python
# Create a tuple
t = (1,2,3)

# Check len just like a list
len(t)

# Tuples Indexing & Slicing
# Indexing and slicing can be used in the same way as strings and lists

t[0]= 'change' # will throw an error as tuples can't are immutable
```

# NamedTuple

- Note that remembering which index to use is tedious for larger codes. 

- Namedtuple assigns name as well as index to each and every member of the tuple

- Format:

  **variable_name = namedtuple(name of the class, list of all the strings which are attributes - each attribute is separated by a space '')**

```python
from collections import namedtuple
#Dog = namedtuple("Dog", "age breed name")
#Dog = namedtuple("Dog", "age, breed, name")
#Dog = namedtuple("Dog", ["age", "breed", "name"])
sam = Dog(age=2, breed = "Lab", name="Sammy")
print(sam)
print(sam.age)
print(sam.breed)
print(sam[1])
print(sam[2])
```

# OrderedDict

* An **OrderedDict** is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that:
* OrderedDict **preserves the order** in which the keys are inserted. A regular dict doesn’t track the insertion order and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.

```python 
# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict
 
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
 
for key, value in d.items():
    print(key, value)
 
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
for key, value in od.items():
    print(key, value)
    
print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)
 
print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)    
```

## Sort OrderedDict by Keys

```python
from collections import OrderedDict

od = OrderedDict()

od['d'] = 1
od['c'] = 2
od['b'] = 3
od['a'] = 4

print(OrderedDict(sorted(od.items())))
```

