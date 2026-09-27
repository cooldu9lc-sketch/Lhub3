## [46\. Permutations](https://leetcode.com/problems/permutations)

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0046-permutations#46-permutations)

### Medium

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0046-permutations#medium)

---

Given an array`nums`of distinct integers, return all the possiblepermutations. You can return the answer in**any order**.

**Example 1:**

**Input:** nums = \[1,2,3\]
**Output:** \[\[1,2,3\],\[1,3,2\],\[2,1,3\],\[2,3,1\],\[3,1,2\],\[3,2,1\]\]

**Example 2:**

**Input:** nums = \[0,1\]
**Output:** \[\[0,1\],\[1,0\]\]

**Example 3:**

**Input:** nums = \[1\]
**Output:** \[\[1\]\]

**Constraints:**

-   `1 <= nums.length <= 6`
-   `-10 <= nums[i] <= 10`
-   All the integers of`nums`are**unique**.

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        res=[]
        def recur(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
            for num in count:
                if count[num]:
                    count[num]-=1
                    recur(curr+[num])
                    count[num]+=1
        recur([])
        return res
```

## [46\. Permutations](https://leetcode.com/problems/permutations)

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0046-permutations#46-permutations)

### Medium

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0046-permutations#medium)

---

Given an array`nums`of distinct integers, return all the possiblepermutations. You can return the answer in**any order**.

**Example 1:**

**Input:** nums = \[1,2,3\]
**Output:** \[\[1,2,3\],\[1,3,2\],\[2,1,3\],\[2,3,1\],\[3,1,2\],\[3,2,1\]\]

**Example 2:**

**Input:** nums = \[0,1\]
**Output:** \[\[0,1\],\[1,0\]\]

**Example 3:**

**Input:** nums = \[1\]
**Output:** \[\[1\]\]

**Constraints:**

-   `1 <= nums.length <= 6`
-   `-10 <= nums[i] <= 10`
-   All the integers of`nums`are**unique**.


```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        res=[]
        def recur(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
            for num in count:
                if count[num]:
                    count[num]-=1
                    recur(curr+[num])
                    count[num]+=1
        recur([])
        return res

```

## [77\. Combinations](https://leetcode.com/problems/combinations)

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0077-combinations#77-combinations)

### Medium

[](https://github.com/cooldu9lc-sketch/Lhub3/tree/main/0077-combinations#medium)

---

Given two integers`n`and`k`, return*all possible combinations of*`k`*numbers chosen from the range*`[1, n]`.

You may return the answer in**any order**.

**Example 1:**

**Input:** n = 4, k = 2
**Output:** \[\[1,2\],\[1,3\],\[1,4\],\[2,3\],\[2,4\],\[3,4\]\]
**Explanation:** There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., \[1,2\] and \[2,1\] are considered to be the same combination.

**Example 2:**

**Input:** n = 1, k = 1
**Output:** \[\[1\]\]
**Explanation:** There is 1 choose 1 = 1 total combination.

**Constraints:**

-   `1 <= n <= 20`
-   `1 <= k <= n`


```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(pos = 1, curr = []):
           ####
        ###The terminating condition is DEPENDENT ONLY ON the size of output, not on i
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(pos, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output
```

<h2><a href="https://leetcode.com/problems/subsets">78. Subsets</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recur(i=0,curr=[]):
            res.append(curr)


            for j in range(i,len(nums)):
                recur(j+1,curr+[nums[j]])

        recur()
        return res
```

<h2><a href="https://leetcode.com/problems/subsets-ii">90. Subsets II</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span><em> (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting will help us to skip a number that have been
        # already used at i-th position at specific permutation.
        nums.sort()
        ans = []
        def backtrack(i=0, solution=[]):
            
            ###MOST IMPOrtant STEP
            ##sol is added to final ans at EVERY CALL
            ans.append(solution)
            
            for j in range(i, len(nums)):
                # We can re-use numbers, but not at this position
                # and same previous premutation
                if j > i and nums[j] == nums[j-1]:
                    continue
                #solution.append(nums[j])
                backtrack(j+1, solution+[nums[j]])
                #solution.pop()
        backtrack()
        return ans
```
