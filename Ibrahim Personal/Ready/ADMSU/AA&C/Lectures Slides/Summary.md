# Week 1

## Network flows

* Flows of goods on a transportation network

* Flow of electricity through the power grid

* Flow of water through pipes

* Flow of information through a communication network

  

## Max Flow Problem 

* How large a flow can we fit through a network

## Residual Network

* Given a network G and flow f, we construct a residual network Gf, representing places where flow can still be added to f, including placed where existing flow can be cancelled.
* For each edge e of G, Gf has edges:
  * e with capacity Ce-fe (unless fe=Ce)
  * opposite e with capacity fe (unless fe=0)

## Residual Flow

* Given network G, flow f. Any flow, g on Gf can be added to f to get a new flow on G
* Flows on Gf are exactly ways to add flow to f

## Cut

* Given a network G, a cut C, is a set of vertices of G so that C contains all sources of G an no sinks of G
* Find a bottleneck for the flow. All flow needs to cross the bottleneck.

## Bound

* Let G be a network. For any flow f and any cut C, |f| <= |C|
* For any cut Cn we get an upper bound on the max flow. Maxflow <= |C|

## Maxflow-Mincut theorem 

* For any network G, max flow |f| = min cut |C|
* For any network G, the maximum overflows of the size of the flow is equal to the minimum over cuts of the size of the cut.
* Can always check if flow is maximal by finding matching cut.
* f a maxflow only if there is no source-sink path in Gf.

## Ford-Fulkerson Algorithm

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\AA&C\Lectures Slides\Images\1.PNG)

### Runtime: 

* Can compute Gf and find P in O(|E|) time. 
* Each time, increase total flow by at least 1.
* Total run time O(|E||f|)
* Note that this algo is not just dependent on the structure of the network but also large capacities hence runtime can be quite large if flow is numerically large.
* Using DFS is fast but not the best, the way path is picked affects the runtime of algo.
* Many iterations will be required if ford-fulkerson selects augmenting path in wrong way

## Edmonds Karp Algorithm 

* Use the Ford-Fulkerson algorithm, always choosing the shortest (in terms of number of edges) augmenting path. Because the longer the path, the smaller the bottleneck value, which results in a longer runtime.
* Hence, find the augmenting paths using BFS instead of DFS. Edmonds karp uses BFS.
* Augmenting flow always saturates (uses all the available flow from) an edge.
* Total runtime = O(|V||E|^2). 
* This is because the Edmonds karp algorithm saturates an edge during each iteration because we are considering the min capacity of an an edge amongst all edges in augmenting path. Hence next time we need to choose a different path which will increase the distance dGf(s, t). But distance dGf(s,t) can only increase |V| times and each time can only have O(|E|) many saturated edges. Therefore only O(|V||E|) many augmenting path.
* And Each path takes O(|E|) time.

## Applications of Max Flow: Bipartite Matching

**Bipartite Graph**

* A bipartite graph is a graph G whose vertex set is partitioned into two subsets, U and V , so that there all edges are between a vertex of U and a vertex of V .

**Matchings**

* Given a graph G , a matching on G is a collection of edges of G , no two of which share an endpoint.

**Bipartite Matching**

* Input: Bipartite graph G 
* Output: A matching on G consisting of as many edges of possible (ideally pairing up all the vertices).

**Applications of Bipartite Matchings**

* Matchmaking
* Scheduling

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\AA&C\Lectures Slides\Images\2.PNG)



# Week 2

## Linear Programming. What is it ?

* Linear programming is nothing but minimizing/ maximizing a linear function of variables subject to a bunch of linear inequality constraints.

* LP is a method to achieve best outcome in a model with constraints represented by linear relationships.

* Linear programming asks for real numbers x1, x2,... satisfying linear inequalities:

  * a11x1 + a12x2 + .........+ a1nxn >= b1

    ​											.........

  * am1x1 + am2x2 + ...... + amnxn >= bm

  So that a linear objective v1x1 + v2x2 + ...... + vnxn is as large (or small) as possible.

* Applications: Factory example, Diet Problem, Network flow problem 

## Special Cases of LP

* No Solution: When 0 = 1
* No Optimum : When 0 = 0

## Gaussian Elimination. Row Reduction. Method to solve LP

* We store equation in form of matrix for convenience
* Three basic row operations:
  * Adding 
  * Scaling 
  * Swapping
* Row reduction is nothing but the method of transferring equations into simple standard form using these 3 operations. The idea is to simulate the substitution method.

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\AA&C\Lectures Slides\Images\3.PNG)

**Runtime**

* m equations in n variables.
* min(n,m) pivots.
* For each pivot, need to subtract multiple of row from each other row O(nm) time.
* Total runtime: O(nm(min(n,m)))

## Degrees of Freedom. What is it ?

* Your solution will be subspace. 
* Dimension = Number of non-pivot variables.
* Dimension = num of variables - num of equations

## Convex Polytope

* A Single linear equation defines a hyperplane.
* An inequality defines a half-space.

**Polytope:** 

* Polytopes: A system of linear inequalities defines a region bounded by a bunch of hyperplanes. A polytope is a region in Rn
  bounded by finitely many flat surfaces.
* Important condition: everything must be on one side of each face.

**Convexity:**

* A region 𝒞 ⊂ Rn is convex, if for any x , y ∈ 𝒞 , the line segment connecting x and y is contained in 𝒞 .
* An intersection of halfspaces is convex.

**Convex Polytope:**

* The region defined by a system of linear inequalities is always a convex polytope.

## Important Lemma 0

* An intersection of halfspaces is convex.

## Important Lemma 1 (Separation)

* Let 𝒞 be a convex region and x ̸∈ 𝒞 a point.Then there is a hyperplane H separating x from 𝒞 .

## Important Lemma 2 (Extreme Points)

* A linear function on a polytope takes its minimum/maximum values on vertices.
* Linear function on segment takes extreme values on ends.

## Duality. What is it ?

* An LP always have a dual problem which has opposite objective to that of an LP.



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\AA&C\Lectures Slides\Images\4.PNG)

* Solutions to dual bound solutions to primal.

**Duality Theorem:**

* A linear program and its dual always have the same (numerical) answer.

* The dual program of finding the max network flow is to just find minimum cut.

## Formulations. What is it ?

* Different types of linear programming problems are called formulations.
* Solving one formulation solves all other formulation.
* Different types of linear programming problems (formulations):
  * Full Optimization --> Minimize or maximize a linear function subject to a system of linear inequality constraints (or say that the constraints have no solution).
  * Optimization from Starting Point --> Given a system of LP and a vertex of the polytope, optimize a linear function with respect to these
    constraints.
  * Solution Finding --> Given a system of linear inequalities, find some solution.
  * Satisfiability --> Given a system of linear inequalities determine whether or not there is a solution.

* Equivalence : If you can solve any of these problems, you can solve any other.

## Methods for Solving LP:

### 1. Simplex Method 

* What is it ?. Method of mathematical optimization to solve LP problems.
* Simplex Method is used to find the optimal solution to maximize or minimize the equation cx1 + cx2 + .... subjected to the linear inequalities in the standard form Ax <= b, where x is the vector of length m, A is n x m matrix with coefficients of inequalities and b is the vector with right-hand side of each inequality.
* To find the optimal solution for the vector of length m,all possible combination of m number of linear equations are solved one by one with row reduction method from the total linear equations n + m + 1 (n linear inequalities + m linear inequalities > 0 which is the case most of the time + 1 inequality to find if the solution is infinite). Now these solutions of m values received is plugged in to all n+m+1 linear inequalities and checked if  all the inequalities are satisfied. If yes, then the set of m values which gives the max value of the equation cx1 + cx2 + ...... is the answer to the LP problem.
* Simplex method works on the concept that A linear function on a polytope takes its minimum/maximum values on vertices.
* There can be 3 possible answers to LP problem. 
  * Bounded Solution: Where the finite set of values exists to minimize or maximize the equation cx1 + cx2 + ...
  * No Solution: Where none of the set of variables subjected to the constraint given can maximize the equation
  * Infinite Solution: Where Infinite number of values can maximize the equation
* Check out the solution of the problem 2 from week 2 from AA&C to understand Simplex Method more.
* Check out this video link for short explanation: https://www.youtube.com/watch?v=jh_kkR6m8H8
* Check out this video link for detailed explanation: https://www.youtube.com/watch?v=qxls3cYg8to&t=2132s
* In the worst case we will have n dimensions and n constraints which would cause there to be O(2^n) vertices and hence runtime is exponential O(2^n). In practice we never get those many vertices hence the average runtime is polynomial that is O(n^k), where k is some integer.

#### What is Standard form and what to do if it is not in standard form ?

A standard form of linear programming is when 

1. Objective function is a maximization
2. All variables have non-negativity constraints
3. All constraints are inequalities 
4. All inequalities have the same sign

What to do when LP is not in the standard form ?

1. If problem is to minimize -2x-y, we can convert it to standard form by doing the opposite that is maximizing 2x + y

2. If the variable x in constraints doesn't have the non-negativity constraints

   e.g. Maximize 2x + y subject to x + y <= 4, x + y <= 10, y>=0

   Simply change x to x1-x2 and add x1,x2 >=0 in the constraints. e.g. x1 - x2 + y <= 4, x1 - x2 + y <= 10, y >= 0

3. If the equality constraints exists simply convert it to inequality e.g. x + y = 4 can be converted to x+y<=4 and x+y>=4
4. If inequalities have different sign e.g. x+y<=4 and x+y>=4, simply negate one of them e.g. x+y<=4 and -x-y<=-4

### 2. Ellipsoid Method

* Polynomial time in all cases.

* Has better worst-case performance than simplex. However, is usually slower.

* Ellipsoid solves the satisfiability version of a Linear Program.

  

# Week 3

## Polynomial Vs Exponential	

* n, n^2, n^3 are all polynomial time algorithms. 

## Search Problems

* We give a formal definition to search problem by considering famous boolean satisfiability problem.
* Boolean satisfiability problems can be expressed in terms of a formula in conjunctive normal form. If this formula is satisfied we say there exists a solution to search problems

## Formula in conjunctive normal form

* (x ∨ y ∨ z ) (x ∨ y ) (y ∨ z ) (z ∨ x ) (x ∨ y ∨ z )
* x , y , z are Boolean variables and clauses are disjunctions (logical or) of literals.

## Satisfiability (SAT)

* Input: Formula F in conjunctive normal form (CNF)
* Output: An assignment of Boolean values to the variables of F satisfying all clauses, if exists
* The problem of satisfiability is called canonical hard problems
* SAT solvers are programs which solves satisfiability problem
* Search problem: given an instance I , find a solution S or report that none exists. For example in case of the SAT problem an instance I is a formula in CNF and solution S is a satisfying assignment
* A search problem is defined by an algorithm 𝒞 that takes an instance I and a candidate solution S , and runs in time polynomial in the length of I . We  say that S is a solution to I iff 𝒞 (S , I ) = true
* For SAT, I is a Boolean formula, S is an assignment of Boolean constants to its variables. The corresponding algorithm 𝒞 checks whether S satisfies all clauses of I .

## Easy and Hard Problems

Hard Problems: Ones for which solution cannot be found in polynomial time.

* Travelling Salesman Problem Vs Minimum Search Tree

* Hamiltonian Cycle Vs Eulerian Cycle
* Longest Path Vs Shortest Path
* Integer Linear Programming Vs Linear Programming 
* Independent set in graph Vs Independent set in a tree

## Class NP

* Class P: Easy to solve in Polynomial time 
* Class NP: Easy to verify in Polynomial time
* A search problem is defined by an algorithm 𝒞 that takes an instance I and a candidate solution S , and runs in time polynomial in the length of I . We say that S is a solution to I iff 𝒞 (S , I ) = true. NP is the class of all search problems.
* If P = NP, then all search problems can be solved in polynomial time
* If P != NP, then there exist search problems that cannot be solved in polynomial time

## NP Complete Problems

Definition :

* A search problem is called NP-complete if all other search problems reduce to it.
* meaning if you can solve one such P problem you can solve all the search problems 

## Reductions 

* We say that a search problem A is reduced to a search problem B and write A → B , if a polynomial time algorithm for B can be used (as a black box)  to solve A in polynomial time.

## Showing NP-Completeness

* If A → B and A is NP-complete, then so is B.

## Independent set --> Vertex cover

* Independent set: A subset of at least b vertices such that no two of them are adjacent.
* Vertex Cover: A subset of at most b vertices that touches every edge.

## Lemma

* I is an independent set of G (V , E ), if and only if V − I is a vertex cover of G .

## 3-SAT --> Independent Set

* Design a polynomial time algorithm that, given a 3-CNF formula F , outputs a graph G and an integer b, such that:
  									F is satisfiable, if and only if G has an independent set of size at least b.

## SAT --> 3-SAT

* Transform a CNF formula into an equisatisfiable 3-CNF formula. Equisatisfiable means F is satisfiable for CNF formula if and only if F' is satisfiable for 3 CNF

## All of NP --> SAT

* Show that every search problem reduces to SAT.
* Instead, we show that any problem reduces to Circuit SAT problem, which, in turn, reduces to SAT.

## Circuit-SAT --> SAT

* To reduce Circuit-SAT to SAT, we need to design a polynomial time algorithm that for a given circuit outputs a CNF formula which is satisfiable, if and only if the circuit is satisfiable
* Introduce a Boolean variable for each gate
* For each gate, write down a few clauses that describe the relationship between this gate and its direct predecessors

## Reduction: To Solve any SAT Problem

* To solve an instance I of the problem A:
  * take a circuit corresponding to 𝒞 (I , ·)
  * the inputs to this circuit encode candidate solutions
  * use a Circuit-SAT algorithm for this circuit to find a solution (if exists)

## SAT: Theory and Practice

* Theory: we have no algorithm checking the satisfiability of a CNF formula F with n variables in time poly(|F |) · 1.99
* Practice: SAT-solvers routinely solve instances with thousands of variables

## Solving Hard Problems in Practice

* An easy way to solve a hard combinatorial problem in practice:
  * Reduce the problem to SAT (many problems are reduced to SAT in a natural way)
  * Use SAT solver

## Sudoku Puzzle

* Goal: fill in with digits the partially completed 9 × 9 grid so that each row, each column, and each of the nine 3 × 3 subgrids contains all the digits from 1 to 9
* Reduce the Sudoku puzzle in to CNF formulae which can be fed to SAT solvers
* State-of-the-art SAT-solvers find a satisfying assignment for the resulting formula in blink of an eye, though the corresponding search space has size about 2^729 ≈ 10^220

# Week 4

## Coping with NP Completeness

* If P != NP, then there is no **polynomial time** algorithm that finds an **optimal solution** to an NP-complete problems in **all cases**. But there are ways to tackle these problems 

1. Special cases - Optimal solution in polynomial time for few cases
2. Approximation algorithms - Non Optimal solution in polynomial time for all cases
3. Exact algorithms (Intelligent exhaustive search) - Optimal solution for all cases but not in polynomial time

## Special Cases

* The fact that a problem is NP-complete does not exclude an efficient algorithm for special cases of the problem.
* 2SAT problem and Independent set of a tree (NOT GRAPH) can be solved in linear time

### 1. 2-Satisfiability

* A linear time algorithm for 2-SAT is possible
* I/P: A set of clauses, each containing at most two literals. O/P: Find a satisfying assignment
* Implication is a binary logical operation denoted by ==> and defined by the following truth table 00==>1, 01==>1, 10==>0, 11==>1
* Construct an implication graph for a 2 CNF formula. 
  * for each variable x , introduce two vertices labeled by x and !x
  * for each 2-clause (ℓ1 ∨ ℓ2), introduce two directed edges !ℓ1 → ℓ2and !ℓ2 → ℓ1
  * for each 1-clause (ℓ), introduce an edge !ℓ → ℓ
* Our goal is to assign truth values to the variables so that each edge in the implication graph is “satisfied”, that is, there is no edge from 1 to 0.
* Skew Symmetry and Transitivity
* All variables lying in the same SCC of the implication graph should be assigned the same value. 
* In particular, if a SCC contains a variable together with its negation, then the formula is un-satisfiable. It turns out that otherwise the formula is satisfiable!
* Running time: O(|F|)

### 2a. Maximum independent set in a tree

* I/P: A tree O/P: An independent set (i.e., a subset of vertices no two of which are adjacent) of **maximum size**.
* Safe Move: For any leaf, there exists an optimal solution including this leaf. Hence it is safe to take all the leaves.
* Running time: O(|T|)

### 2b. Maximum weighted independent set in a tree

* I/P: A tree O/P: An independent set (i.e., a subset of vertices no two of which are adjacent) of **maximum total weight**.

* Using dynamic programming solve the sub-problem

* Subproblem - D (v ) is the maximum weight of an independent set in a subtree rooted at v

* Recurrence relation: D (v ) is 

  ​	max { w (v ) + ∑︁ D(w) grandchildren w of v, ∑︁ D(w) children w of v }

## Exact Algorithm 

* Exact algorithms or intelligent exhaustive search involves finding an optimal solution without going through all candidate solutions
* Brute force search algorithm finds an optimal solution enumerating through all possible candidate solutions and selecting the best one



### 3-Satisfiability

* A brute force search algorithm checking satisfiability of a 3-CNF formula F with n variables, goes through all assignments and has running time O (|F| · 2^n).

#### Backtracking

* Main Idea: Construct a solution piece by piece.  Backtrack if the current partial solution cannot be extended to a valid solution
* Thus, instead of considering all 2^n branches of the recursion tree, we track carefully each branch. The maximum possible number of leaves in the recursion tree of a backtracking algorithm solving satisfiability of this formula is 2^n - k + 1

#### Local Search

* Main Idea: Start with a candidate solution. Iteratively move from the current candidate to its neighbor trying to improve the candidate
* Hamming distance (or just distance) between two assignments 𝛼, 𝛽 ∈ {0, 1}^n is the number of bits where they differ: dist(𝛼, 𝛽 ) = |{i : 𝛼i != 𝛽i}|.
* Hamming ball with center 𝛼 ∈ {0, 1}^n and radius r , denoted by ℋ(𝛼, r ), is the set of all truth assignments from {0, 1}^n at distance at most r from 𝛼.
* Lemma: Searching a Ball for a Solution : Assume that ℋ(𝛼, r ) contains a satisfying assignment 𝛽 for F . We can then find a (possibly different) satisfying assignment in time O (|F | · 3^r).
* Assume that F has a satisfying assignment 𝛽
* If it has more 1’s than 0’s then it has distance at most n/2 from all-1’s assignment
* Otherwise it has distance at most n/2 from all-0’s assignment
* Thus, it suffices to make two calls: CheckBall(F , 11 . . . 1, n/2) and CheckBall(F , 00 . . . 0, n/2)
* The running time of the resulting algorithm is **O (|F | · 3^n/2) ≈ O (|F | · 1.733^n)**

### Travelling Salesman Problem

* Input: A complete graph with weights on edges and a budget b. Output: A cycle that visits each vertex exactly once and has total weight at most b.
* A naive algorithm just checks all possible (n − 1)! cycles.
* Dynamic programming to solve TSP is O (n^2· 2^n)

#### Dynamic Programming

* We are going to use dynamic programming: instead of solving one problem we will solve a collection of (overlapping) subproblems.
* For a subset of vertices S ⊆ {1, . . . , n} containing the vertex 1 and a vertex i ∈ S , let C (S , i ) be the length of the shortest path that starts at 1, ends at i and visits all vertices from S exactly once
* C ({1}, 1) = 0 and C (S , 1) = +∞ when |S| > 1
* Consider the second-to-last vertex j on the required shortest path from 1 to i visiting all vertices from S
* The subpath from 1 to j is the shortest one visiting all vertices from S − {i} exactly once
* Recurrence Relation : C (S , i ) = min{C (S − {i}, j ) + dji}, where the minimum is over all j ∈ S such that j != i

#### Branch and Bound

* The branch-and-bound technique can be viewed as a generalization of backtracking for optimization problems.
* Backtracking is usually used for solving decision problems while branch and bound is used to solve optimization problems.
* We grow a tree of partial solutions. 
* At each node of the recursion tree we check whether the current partial solution can be extended to a solution which is better than the best solution found so far.
* If not, we don’t continue this branch.

## Approximation Algorithms

### Vertex Cover

* Input: A graph, Output:  A subset of vertices of minimum size that touches every edge.

* ApproxVertexCover(G (V , E )): Remove edges from E and add vertices u, v. Remove from E all edges incident to u, v

* The algorithm ApproxVertexCover is 2-approximate: it returns a vertex cover that is at most twice as large as an optimal one and runs in polynomial time.

* Any vertex cover of the graph has size at least |M|. The algorithm returns a vertex cover C of size 2|M|, hence

  ​				|C| = 2 · |M| ≤ 2 · OPT

* We don’t know the value of OPT, but we’ve managed to prove that |C | ≤ 2 · OPT

* This is because we know a lower bound on OPT: it is at least the size of any matching |C| = 2 · |M| ≤ 2 · OPT

* The bound is tight: there are graphs for which the algorithm returns a vertex cover of size twice the minimum size. Example Bipartite graph.

* No 1.99-approximation algorithm is known.

### Travelling Salesman 

#### Metric TSP (Optimization version)

* Metric means it has to satisfy the triangle inequality: for all u , v , w ∈ V ,d (u , v ) + d (v , w ) ≥ d (u , w)
* We are going to design a 2-approximation algorithm: it returns a cycle that is at most twice as long as an optimal cycle: C ≤ 2 · L ≤ 2 · OPT
* Let G be an undirected graph with non-negative edge weights. Then MST(G ) ≤ TSP(G). We are going to use MST as L. By removing any edge from an optimum TSP cycle one gets a spanning tree of G.
* The algorithm ApproxMetricTSP is 2-approximate.
* The currently best known approximation algorithm for metric TSP is Christofides’ algorithm that achieves a factor of 1.5.

#### Local Search

* Find the better solution from some initial solution 
* Trade-off between quality and running time of a single iteration
* Still, the number of iterations may be exponential and the quality of the found cycle may be poor
* But works well in practice

