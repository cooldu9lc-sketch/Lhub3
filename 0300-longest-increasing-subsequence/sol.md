**Solution 4: Binary Indexed Tree (Increase BASE of`nums`into one-base indexing)**

-   Let`f[x]`is the length of longest increase subsequence , where all number in the subsequence <=`x`. This is the max element in indices`[1..x]`if we build the**Binary Indexed Tree (BIT)**
-   Since`-10^4 <= nums[i] <= 10^4`, we can convert nums into`1 <= nums[i] <= 2*10^4+1`by plus`BASE=10001`to store into the BIT.
-   We build**Max BIT**, which has 2 operators:
    -   `get(idx)`: Return the maximum value of indices in range`[1..idx]`.
    -   `update(idx, val)`: Update a value`val`into BIT at index`idx`.
-   Iterate numbers`i`in range`[0..n-1]`:
    -   subLongest = bit.get(nums\[i\] - 1) // Get longest increasing subsequence so far, which`idx < nums[i]`, or`idx <= nums[i] - 1`.
    -   bit.update(nums\[i\], subLongest + 1) // Update latest longest to the BIT.
-   The answer is`bit.get(20001)`// Maximum of all elements in the BIT