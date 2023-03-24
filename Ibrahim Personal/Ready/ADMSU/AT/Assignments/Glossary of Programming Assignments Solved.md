# Glossary of Programming Assignments Solved

# Week 1

### 1. Sum of two digits

### 2. Maximum Pairwise Product

# Week 2

### Theory

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Big-O Quiz.PNG)

* Notice that Big-O is upper bound. Big-Omega is lower bound and Big-theta is both upper and lower bound to the running time.https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation

### 1. Fibonacci Number

* Recursive: 
  * Recursion Read: https://www.coursera.org/learn/algorithmic-toolbox/lecture/vNEfl/problem-overview-and-naive-algorithm
  * Running time: T(n) = 2 if n <= 1 or T(n-1) + T(n-2) + 3 otherwise
  * Time Complexity = O(n^2). See lecture 8 if not clear.
  * ![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Big-O.PNG)
* Loop based:
  * Running time: T(n) = 2n + 2
  * Time Complexity: O(n)



### 2. Last Digit of a Large Fibonacci Number 

### 3. GCD of a Number

* Naive Algorithm
* Efficient Algorithm
* Remember this Lemma

```c++
/*
Let a′ be the remainder when a is divided by b, then

gcd(a, b) = gcd(a′, b) = gcd(b, a′).
*/
```

### 4. Least Common Multiple

* Remember this lemma

```c++
/* 
a x b = lcm x gcd
*/
```

### 5. Fibonacci huge

* Concept of Pisano length should be used
* https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836

### 6. Last digit of the sum of Fibonacci number

* Notice that last digit of a Fibonacci number repeats after the length of 60. Hence we have a set of 60 numbers which will get repeated over and over again.

### 7. Last digit of the sum of Fibonacci numbers again

* Same as previous one just take the sum of the last numbers in the range given by the user and then find the last digit of that sum.

### 8. Last digit of the sum of squares of Fibonacci number

* Same as previous with minor tweaks.

# Week 3 - Greedy Algorithms

### Theory

**[1] 3 steps to solve greedy algorithms.**

1. Make some greedy choice. Make a first move
2. Reduce to a smaller subproblem. Then solve a problem of the same kind using safe move.
3. Iterate

* Subproblem is a similar problem of smaller size.
* A greedy choice is called safe move if there is an optimal solution consistent with this first move.
* Largest number and Car Fueling are some of the examples of Greedy
* Running time of Car Fueling (MinRefills(x, n, L)) is O(n)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Greedy.PNG)

**[2] Grouping Children :**

* Naive algorithm works in time Ω(2 n )

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\grouping children Naive.PNG)

* Efficient Algorithm - PointsCoverSorted.
* The running time of PointsCoverSorted is O(n).

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Greedy - Pointscoveredsorted.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Grouping Children - Total running time.PNG)

**[3] Fractional Knapsack**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Knapsack safemove.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Knapsack Algorithm.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Knapsack Algorithm 2.PNG)



* Running time of Knapsack is O(n^2). But we can sort the max value per unit item in best possible time of nlog(n) hence total time will be nlog(n) + n ~ nlog(n)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Knapsack running time 1.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Knapsack running time 2.PNG)

### 1. Money Change

### 2. Maximum Value of the Loot

### 3. Car Fueling

### 4. Maximum Advertisement Revenue

### 5. [Not Solved] Collecting Signatures 

### 6. Maximum Number of Prizes

* Generate a vector where each digit is the sum of all the preceding digits till the element is obtained which is greater then n.
* Last element in the question will be summands[i-2] + summands[i-1] hence remove last two elements and replace it by this sum

### 7. Maximum Salary

* Main idea is find the max number which can be formed from two numbers which does not have equal number of digits is to concatenate them in both directions and see which one is greater.
* Eg to get the max no created from 22 and 3 options are 223 and 322 from which 322 is greater. Note that we will get answer 223 if we just sort the elements in decreasing order

# Week 4 - Divide and Conquer Algorithms

* Break into non-overlapping subproblems of the same type.
* Solve subproblems. Combine results.

### Theory

**Linear Search**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Recursive 1.PNG)

* A recurrence relation is an equation recursively defining a sequence of values.
* Recurrence defining worst-case time: T(n) = T(n − 1) + c
* Time complexity O(n) = n

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Recursive 2.PNG)

**Binary Search**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Recursive 3.PNG)

* Recurrence defining worst-case time: T(n) = T(n/2) + c
* Time complexity O(n) = log2(n) = log(n)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Recursive 4.PNG)

**Polynomial Multiplication - Naïve Algorithm **

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Poly Mul Naive.PNG)

* Recurrence: T(n) = 4T(n/2) + kn
* Run time - Theta(n^2)

**Polynomial Multiplication - Naïve Divide and Conquer Algorithm **

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Poly Mul Naive divide and conquer.PNG)

**Polynomial Multiplication - Faster Divide and Conquer Algorithm (Karatsuba approach) **

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Poly Mul karatsuba.PNG)

* **Run time - Theta(n^1.58)**

**Master Theorem**

* Helps predict running time from recurrent relation without creating recurrence tree, figuring out how much work needs to be done at each level and then sum up this work.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Master Theorem.PNG)

**Selection Sort**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Selection_Sort.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Selection_Sort_runtime.PNG)

* Notice that the estimation is too Pessimistic. As i grows, the number of iterations of the inner loop decreases: j iterates from i+1 to n.
* A more accurate estimate for the total number of iterations of the inner loop is (n-1) + (n-2) + .... + 1

**Merge Sort**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Merge Sort.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Merge Sort running time.PNG)

* Merging both halves takes linear time O(n).
* 2T(n/2) represents time taken to sort the array if size n/2.
* O(n) is the time before splitting the array and after merging the array.
* Hence Recurrence relation T(n) = T(n/2) + O(n)

**Lower Bound for Comparison Based Sorting**

* Selection sort and merge sort are comparison based.
* Any comparison based sorting algorithm performs Ω(n log n) comparisons in the worst case to sort n  objects.

**Decision Tree - Estimating Tree Depth**

* Number of leaves ℓ in the tree must be at least n! (the total number of permutations)
* Worst-case running time of the algorithm (the number of comparisons made) is at least the depth d
* d ≥ log2ℓ (or, equivalently, 2d ≥ ℓ). Max number of leaves in the tree will be less than 2d

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Comparion based Algo running time.PNG)

**Non-Comparison Based Sorting Algorithms**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Non-Comparison Based Sorting Algorithms.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Non-Comparison Based Sorting Algo running time.PNG)

**Quick sort Algorithms**

* Another Comparison based Algorithm.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_1.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_2.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_3.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_5.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_6.PNG)

* Running time is proportional to the number of comparisons made.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_7.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_8.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_9.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_10.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\Quicksort_11.PNG)

### 1. Binary Search

### 2. Majority Element

* Take a look. Very Interesting

### 3. Improving Quick Sort

### 4. Number of Inversions

### 5. Organizing a Lottery

* Take a look. Very Interesting

### 6. Closest Points



# Week 5 - Dynamic Programming 1

### Theory

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_1.PNG)

* Greedy solution is not always optimal. Example coin change.
* Hence recursive solution can be helpful but takes too long.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_2.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_3.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_4.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_5.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_6.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_7.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_8.PNG)

* Maximizing the length of a common subsequence corresponds to maximizing the score of an alignment with 𝜇 = 𝜎 = 0.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_9.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_10.PNG)

**Computing Edit Distance**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_11.PNG)



**Let D (i , j ) be the edit distance of an i -prefix A[1 . . . i ] and a j -prefix B [1 . . . j ]**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_12.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_13.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_14.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_15.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_16.PNG)



### 1. Money Change Again





# Week 6 - Dynamic Programming 2

**Problem Overview - Knapsack Problem** 

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_17.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_18.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_19.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_20.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_21.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_22.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_23.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_24.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_25.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_26.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_27.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_28.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_29.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_30.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_31.PNG)

**Placing Parentheses**

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_32.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_33.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_34.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_35.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Algortihms ToolBox\Images\DP_36.PNG)

