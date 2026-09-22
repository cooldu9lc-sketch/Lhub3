## This works because of 2 conditions
> 1) mask==2**n-1 in dp makes sure all elements are used. 
> 2) dp(2**n-1)==0 makes sure sum of all elements divided by target_sum is zero

# Core Idea
Instead of tracking:

```
howmanysubsetshavebeencompleted
```

the trick is:

Store only:

```
current_sum%target
```

# What does dp\[mask\] mean?

The most important idea:

```
dp[mask]
```

means:

> After selecting the elements represented by mask,
> what is the current partial sum inside the subset we are currently filling?



# Why Sort Descending?

```
arr.sort(reverse=True)
```

Example:

```
[5,4,3,3,2,2,1]
```

If a large number cannot fit somewhere, we discover failure quickly.

This is a pruning optimization.


## Why Does This Work?
-   completed subsets do not need to be counted explicitly
-   modulo automatically starts a new bucket
-   2**n-1 in dp makes sure all elements are used. dp(2**n-1)==0 makes sure sum is zero
-   full mask + remainder 0 implies all k subsets were formed