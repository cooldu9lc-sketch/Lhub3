The original problem statement is equivalent to:
Find a**subset**of`nums`that need to be positive, and the rest of them negative, such that the difference is equal to`target`

Let `P`be the positive subset and`N`be the negative subset

Then let's see how this can be converted to a subset sum problem:

```lisp
                  sum(P) - sum(N) == 0 
                 or Sum(P) should be the closet Value possible to Sum(nums/2) so that the difference between two sums is minimised
2 * sum(P) = target + sum(nums)
```

So the original problem has been converted to a subset sum problem as follows:
Find the**subset**`P`of`nums`such that`sum(P) is the max Value <= sum(nums)//2`

Refer LC: 416 To Solve Subset Sum and  LC 494