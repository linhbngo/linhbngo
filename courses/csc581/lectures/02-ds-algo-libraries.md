# Data structures and supporting libraries

## 1. Overview and motivation

- Data Structures: a mean to store and organize data. 
- Pick an appropriate DS that support efficient insertions, searches/queries, deletions, and updates. 
- Assumption: familiarity with the data structures discussed in the remainder of this episode. 
- You only need to **know enough** so that you can **select** and **use** the **correct data structures**.
  - Understand the strengths, weaknesses, and time/space complexities. 
  



## 2. Linear Data Structure: Array
- Many builtin support for Java/C++. We focus on Java for this class. 
- Static Array: [Builtin supports in Java](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Arrays.html)
- Dynamic Array: [ArrayList](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayList.html)
- Sorting: 
  - Java Array has builtin sort. 
  - ArrayList: inherits `sort` from [Java Collections](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collections.html)
  - `O(n^2)`: Bubble, Selection, Insertion
  - `O(nlog(n))`: Merge, Quick, Heap
  - `O(n)`: Counting, Radix, Bucket
- Searching (on a sorted linear data structure):
  - `O(n)`: linear search
  - `O(log(n))`: binary search ([Java Collections](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Collections.html))
- Array of Booleans: [Java BitSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/BitSet.html)



## 3. Special Sorting Problems
- Inversion Index: count the number of swap to make a list into a sorted order
  - `O(n^2)`: actual runs bubble sort. 
  - `O(nlog(n))`:
    - Modification of Merge Sort: increment count by one when the `front right` is selected in the merging process before the `front left`. 
 <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2021-12-31T15:41:38.018Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\&quot; etag=\&quot;kGsr5DqedpS355VpiMjx\&quot; version=\&quot;15.8.6\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;-DU5byVVsSvFbV76346P\&quot; name=\&quot;Page-1\&quot;&gt;7VpLc5swEP41HNNBEi8fG8ckPbQ9ODM9M0YBGmwRgePHr68wAgwiE3ccC2Hji/Hqsfjb3U+rlTQ0XW4fqZeEP4mPYw3q/lZDDxqEABk6+8olu0JiIacQBDTyeadaMI/2mAv5uGAd+ThtdMwIibMoaQoXZLXCi6wh8yglm2a3FxI3tSZegAXBfOHFovRP5GdhIXVMvZY/4SgIS81A5y1Lr+zMBWno+WRzJEIzDU0pIVnxtNxOcZyDV+JSjHM/aK1ejOJVdsqA58fQd/f799ent+TH31+/Z8+L/R2f5d2L1/wPIw1aMZvwPk28Vf7a2Y5jYb2t83e934RRhu9Y84LJv+fvQHHdyp4C/q1BNCme4kLiFnMWHQxZimxZiixZioAsRVCWIkeWIpMHYzU/pGS98nEeJHqpZl5oedgwTmOyMFvG7Bc4zHYIF0wzvP0wDkEV3YwWMVnijO5YFz4AWpwQOCOWDLmp6QXa/DXDI2pBvJ/HGS2oZq6Dnj3wuP8PDoACB4z+NWD/Mlr+Va1IRw4GSqeT4mBoXGS+dJHp2cHARDUHMwQHuyFzwLY5bNEctkxrmL2Ge9/B0Wbfvq1hCda4obXQVM0adq+5Vt+ZCTTVsobTxVR9E4jRdNmu/YHUxXUigNQ/y1blIVVAAmIhxT4PpTSj5BVPSUzoYTRyXZ19qpayGgW/CFFbNUTFbemZuZZkRJFqgQzEfRjoPZIN3VQMJXEzocDKaauGkpjkO4OKTlO56BQT9TPzZ8mIWsqtyWKyLa1CP7DFv1VCQEA0ndTEHHRm5rdaQ+jfHOIewJRYuR9QJLULDr2brjx9HisOaphD3Cde32HbyA0nHcwhp+9zk3Jnc9Unc2POd9IpngLe2FmfuDJuvL74ksb2MgN5XL9OuLjUcXwj+eaSWKsTK5psnihJ8edwemlS3CB9iba5CUR8dd12XfdS+CLQKvJ1MDLsIGR4MXjFIp+Y0g8GXtPRFYNXrPiJx4+DgRc59rem/xroYgCzn/XF6UPb0fVzNPsH&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div><script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
- Sorting in linear time:
  - Depending on data type
  - `O(n + k)` Counting Sort
  - `O(d * (n + k))` Radix Sort



## 4. Linear Data Structure: Bitmask
- Use an signed interger to represent a `lightweight` small set of Boolean values. 
- This is faster than the `BitSet` class of Java. 
- Limitation: up to 64 items only. 
- Example: S = 34 
  - Binary: `1 0 0 0 1 0`
  - Index: `5 4 3 2 1 0`
  - Power of 2: `32 16 8 4 2 1`
  - Alphabet: `F E D C B A`.
  - S can represent `{1, 5}` or `{F, B}` or `{32, 2}`.
- To multiply/divide by 2, shift all bit left/right one:
  - `<< 1`: multiply by 2/shift left 1
  - `<< 2`: multiple by 4/shift left 2
  - `>> 1`: divide by 2/shift right 1. 
- To set (turn on) the bit at position `j`, use bitwise OR: `S = S | (1 << j)`
  - `1 << j` will shift 1 forward `j` position, every other bits remain 0. 
  - A bitwise OR of the above result with S will set the bit value of S at position `j` to 1. 
- To check if the bit at position `j` is on, use bitwise AND: `T = S & (1 << j)`.
  - `T == 0`: `j` bit is 0
  - `T != 0`: `j` bit is 1
- To clear/turn off the bit at position `j`: `S = S & ~(1 << j)`
- To flip the bit at position `j`: `S = S ^ (1 << j)`
- To get the value of the least significant bit of S that is on: `T = ((S) & -(S))`
  - Negative S, not flipped bits of S. 
- To turn on all bits in a set of size `n`: `S = (1 << n) - 1`



## 5. UVa problem 11173: Gray Codes
[Problem's link](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=23&page=show_problem&problem=2114)

 ## Initial description (after taking away the bells and whistles)
 - You will be given total number of cases: `N <= 250000`
 - For each case:
   - You will be given number of bits: `1 <= n <= 30`
   - You will be given the `k` position of the `n-bit` Reflected Gray Code: `0 <= k <= 2^n`. 
 - Run time is most likely an issue to be considered here. 


 ## Input/output format:
 - Type 1: The number of cases is given in the first line
 - Each case involves parsing two integers.   
 - Nothing special for output.  


 ## Thought process:
 - Bit operations would be fastest. 
 - Textbook suggestion: one-liner bit manipulation expression. 
 - What is the pattern here?
   - Do not look at the value of the bits, it is the output, not the pattern. 
 <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2021-12-31T17:48:57.463Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\&quot; etag=\&quot;RwZVGS4MI67aokTCkPQs\&quot; version=\&quot;16.1.2\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;cctGU62Ts0LgoPzjfe7G\&quot; name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div><script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
 - If an even bit is set, the flip the next bit?
   - Not good enough. 
 - XOR patterns, can you see it?


 ## Accepted solution
 <script src="https://gist.github.com/linhbngo/3529c879f8375d9e7eb29f355805bc0c.js?file=11173.java"></script>
{:.solution}



## 6. Big Integer
- Use [Java's BigInteger](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigInteger.html) for this purpose




## 7. Linked Data Structures

- [Java LinkedList](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/LinkedList.html)
- [Java Stack](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Stack.html)
- [Java Queue](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Queue.html)
- [Java Double-ended Queue](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Deque.html)
- Stack-based problems:
  - Bracket matching
    - [Valid parentheses](https://leetcode.com/problems/valid-parentheses/)
    - [Check if a parentheses string can be valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)
  - Postfix Calculator




## 8. UVa problem 12150: Pole Position
[Problem's link](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=243&page=show_problem&problem=3302)

 ## Initial description (after taking away the bells and whistles)
 - Initial array: car number at each index. 
 - Subsequent array: car numbers and their relative displacement. 
  


 ## Input/output format:
 - First value is the `N` number of cars. 
   - Next `N` pairs are the cars and their relative displacement. 
   - Repeat with a new `N` until `N` == 0. 
 - N between 2 and 1000
 - C between 1 and 10000
 - P between -1000000 and 1000000



 ## Thought process:
 - Initial visualization: 
   - 2-dimensional array, 1 column for car number and 1 column for relative positions. 
   - Imagine the starting position, the entire second column would be 0s.  
 - Input data contain the cars at **new index position** (first column), and **displacement** from initital positions.  
   - Current index **plus** (or **minus**?) displacement will provide initial position. 
 - Do we actually need a 2-dimensional array?  
 - What are the possible edge cases for invalid starting positions? 
  


 ## Accepted solution
 <script src="https://gist.github.com/linhbngo/3529c879f8375d9e7eb29f355805bc0c.js?file=12150.java"></script>





## 9. Challenges

- Kattis: [Baloni](https://open.kattis.com/problems/baloni)
- Kattis: [Greedily Increasing Subsequence](https://open.kattis.com/problems/greedilyincreasing)
- Kattis: [Mastermind](https://open.kattis.com/problems/mastermind)



## 10. UVa problem 11581: Grid Successors
[Problem's link](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2628)

 ## Initial description (after taking away the bells and whistles)
 - 3x3 grid, each cell containings 0 or 1 
 - Function `f` is the standard cell-based transformation that is similar to the 
 [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)'s principle: 
 Each cell's transformation depends on the adjacent cells. 
   - Sum of adjacent cells modulo 2: resulting values will be 0 or 1. 
   - Needs to pay attention to border cells. 
  - The recursive function starts from the original grid, and there is a chance that 
  over time, it will transform one of the subseqeuent grid back to the original grid. 
 - The value i = k<sub>g</sub>(h) such that h=f<sup>(i)</sup>(g)
   - Therefore: k<sub>g</sub>(f<sup>(i)</sup>(g)) means the number of steps `i` so that function `f` 
   transforms `g` back to itself. 


 ## Input/output format:
 - First value is the `N` number of grids. 
 - Each group of subsequent four lines:
   - One empty line. 
   - Three lines, each of which is a string of three characters, either `0` or `1`. 



 ## Thought process:
 - Should have a separate method for `f`. 
 - To know when `g` is transformed back to itself, this means we need to 
 keep track of the past data structures.   
 - Identify the finiteness of `i` is easy: we only need to know when the current grid matches the original grid. 
 - Identify the infinite case (ouptut of -1) is the question.   
   - Going back to the finite case, if the grid is transformed back to itself after `i` steps, this means 
   there is another circular tranformation back to itself after an additional `i` steps.  
   - If there exists a `circular transformation` that does not contain the original grid, this means 
   we have hit the infinite case. 
 - Implication: we need to know if the current grid matches **any** of the previous grid arrangement. 
 - The question: is the number of possible grid arrangement finite or infinite?  
   - Recall: Bitmask
 <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2022-01-03T15:03:17.272Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\&quot; etag=\&quot;YNsDlmREQGCxvj0BWpG_\&quot; version=\&quot;16.1.2\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;NN6JLIPQCRtrRHx7-tS3\&quot; name=\&quot;Page-1\&quot;&gt;7ZrRjqIwFIafhss1pQXUyx0dx5tNJvFi97YLFUjQklIV9+m3LAXE1nVWmUKymEwsh3KK339G+5daaLHL3xhOo280IIkFQZBbaGlBaDtTT7wVkXMZmXugDIQsDmSnJrCJfxEZrLod4oBkrY6c0oTHaTvo0/2e+LwVw4zRU7vblibtUVMcEiWw8XGiRr/HAY/K6MwFTXxN4jCqRraBPLPDVWcZyCIc0NNFCL1aaMEo5WVrly9IUsCruJTXrW6crW+MkT3/yAXb9fo9fzv+2OLdHsDV4WUF2BeZ5YiTA6mTAPnnJSLxy08mWmHR+sspW56S+TJ+rgCeopiTTYr94vgkikT0jvguEUe2aOIsLWXbxjkRd/oib4gwTvKbn9Su+YnCI3RHODuLLvICRxKXJedVCpwaASv9ogvtqhiWJRPWiRuqoiHB/gNk2DFkMEDIrt0zZNQRZFnFg6xkB/QM2ekY8hArGc57hux2CHmo38n2rGfIXseQh1jJ054ZTxXGCiQxKUqL5jYh+ddiuiZAkH0gm0s/wVkW+21yjB72QYFsCWpsJFCmcXehfRALIwnm8bGdXsdKjvBOYzFwrYnnTNx26aMr3hk9MJ/Iyy4ncHczTa8yccxCwpVMf8SrP/jjes5GPTUqeLOu9JxCs3rORz01KrjX/1UP6+nZZvWshhsFbcngeF0J6gLDgqr2fBQUQnQ9Y3lYUDQ3LKi6FDAKCpuJ69OCwusf488WVHXEk8lE0XQAXsDp2QxAdbYBqpfCq13Pd+h1AMv22rQ07rRe2L2kdT2V7241S62r//CLAoJ5V+ZJk8qwe0Lqus4oqfWEf1JTmTZQSF1FGiW1nrBQmuow7KHQuGil1eFhE6WpDsMuCo3rVlodHrZRmlSGfRQal660OjxspDSpDDup6s41/kB9gNW3P7A1zwjNGgRHs3ND0hqenUKa59aGccGbuIZXXY5mL4VhXJrdFLK4hlddrmZ/j2Fcmn0REtfwqstDveNSnbBu0axvUFP380CJw2bnX/kT2uyfRK+/AQ==&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div><script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
   - With 9 bits, maximum possible grid arrangements = 2<sup>9</sup> = 512


 ## Accepted solution
 <script src="https://gist.github.com/linhbngo/3529c879f8375d9e7eb29f355805bc0c.js?file=11581.java"></script>





## 11. Challenges

- Kattis: [Nine Knights](https://open.kattis.com/problems/nineknights)
- LeetCode: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- LeetCode: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- LeetCode: [Jump Game](https://leetcode.com/problems/jump-game/)
- Kattis: [Epig Dance Off](https://open.kattis.com/problems/epigdanceoff)
- Kattis: [Flowshop](https://open.kattis.com/problems/flowshop)




## 12. Non-linear Data Structures: Binary Heap (Priority Queue)
- [Java PriorityQueue](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/PriorityQueue.html).
  - From node `i`:
    - To parent: `floor(i)` or `i>>1`
    - To left child: `2 * i` or `i<<1`
    - To right child: `2 * i + 1` or `(i<<1) + 1`
- Heap property:
  - Items on left and right subtree of root `x` are always smaller than `x`. 
  - The root is always the max-value item. 
- Highest value-item can be dequeued in `log(n)` time. 
- New item can be enqueue in `log(n)` time. 
- Important components for:
  - Prim's and Kruskal's algorithms for minimum spanning tree. 
  - Dijkstra's Single Source Shortest Path. 



## 13. Kattis problem: Knigs of the Forest
[Problem's link](https://open.kattis.com/problems/knigsoftheforest)
- Hint: PriorityQueue
  - Two queues
  - Rewrite comparator to custom compare. 
  - [Writing custom comparator](https://www.callicoder.com/java-priority-queue/)
  - [More description on comparator - how do they compare?](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Comparator.html)

 ## Accepted solution
 <script src="https://gist.github.com/linhbngo/3529c879f8375d9e7eb29f355805bc0c.js?file=kattis_knigsoftheforest.java"></script>





## 14. Challenges

- Kattis: [Stock Prices](https://open.kattis.com/problems/stockprices)




## 15. Hash Table
- [Java HashMap](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/HashMap.html)
- [Java HashSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/HashSet.html)
- What we did in JollyJumper, TreasureHunt, ... could be considered a simple naive form 
of hashing called `Direct Addressing Table`. 




## 16. Kattis problem: Quick Brown Fox
[Problem's link](https://open.kattis.com/problems/quickbrownfox)
- Hint: Direct Access Table
  - 1 if 0, no action otherwise.
  - Check sum and reset.  


 ## Accepted solution
 <script src="https://gist.github.com/linhbngo/3529c879f8375d9e7eb29f355805bc0c.js?file=kattis_quickbrownfox.java"></script>





## 17. Challenges

- Kattis: [What does the fox say?](https://open.kattis.com/problems/whatdoesthefoxsay)




## 18. Balanced Binary Search Tree (bBST)
- Binary Search Tree implemented using  ADL (Adelson-Velskii Landis) or Red-Black
implementation. 
- [Java TreeMap](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/TreeMap.html)
- [Java TreeSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/TreeSet.html)
- Insertion/search/removal: `log(n)` time. 
- use bBST as a PriorityQueue ADT: `lastKey` for max value, `firstKey` for smallest value. 



## 19. Order Statistics Tree
- Selection: Find the k<sup>th</sup> smallest element of an array of n element. 
- Ranking: If the k<sup>th</sup> smallest element is `v`, then ranking of `v` is `k`. 
- Selection problem, static data:
  - `k=1` and `k=n`: manual comparison, best run time is `n`. 
  - For other cases: sort then compare, run time `nlog(n)`.
  - Best `n` algorithm: Utilize `RandPartition` of [QuickSort](https://docs.google.com/presentation/d/1oO-d_NrVzSvZ1cvoKvbrL3wHQJSeHGOpTdTud2FjCb0/edit#slide=id.p):
    - `q = RandPartition(A, 0, n-1)`, all element `<=` A[q] will be placed before
    the pivot, so A[q] will be in its correct order statistics, which is `q+1`. 
- Selection problem, dynamic data:
  - Construct a bBST
  - Preprocessing: `nlog(n)`
  - Actual answer: `log(n)` by traversing down the tree. 


