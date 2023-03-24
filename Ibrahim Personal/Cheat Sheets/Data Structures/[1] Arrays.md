# Arrays

* Contiguous area of memory consisting of equal-size elements indexed by contiguous integers.
* Constant time access to any element: array_addr + elem_size x (i - first_index)
* Constant time to add/remove at the end. Linear time to add/remove at an arbitrary location. 

![Lightbox](https://media.geeksforgeeks.org/wp-content/uploads/C-Arrays.jpg)

## Time for common Operations

|       Operations       | Add  | Remove |
| :--------------------: | :--: | :----: |
| **Insert @ Beginning** | O(n) |  O(n)  |
|    **Insert @ End**    | O(1) |  O(1)  |
|  **Insert @ Middle**   | O(n) |  O(n)  |

## When to Use ?

* Arrays are used **when there is a need to use many variables of the same type**.

## Python Implementation 

* List is most commonly used to implement arrays in python. Although Tuples can also be used.

```python
lst_1=[1,2,3]
lst_2=[4,5,6]
list_1.append(7)
list_1.pop()
lst_1.sort() # inplace meaning it doesn't return anything
list_1.reverse() # inplace meaning it doesn't return anything
matrix = [lst_1,lst_2] # Make a list of lists to form a matrix
matrix[0][0] # Grab first item of the first item in the matrix object
mylist = [x for x in range(0,11)] # List Comprehension
x = [1,2,3]
x.count(3)
x.append([4, 5])
x.extend([4,5])
```

