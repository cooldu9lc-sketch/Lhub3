Greedy:

We must think about sorting`pairs`if we want to solve the problem using a greedy strategy, which involves picking up pairs on the fly from the beginning to the end whenever we can.

Let's see what happens if we order the "pairs" based on the first element and then pick pairs whenever we can in order. Take the pairs`[1, 10], [2, 4], [5, 8], [9, 11]`as an example. They are ordered according to the first element.

An incorrect answer of`1`will be returned if we choose the first element and keep choosing the pairs as we go. The correct answer is`3`.

This suggests that sorting based on the first element wouldn't be effective because the second element of a selected pair might be large enough to prevent the addition of numerous additional pairs.

Note that sorting based on the first element worked with the earlier methods because we built the solution optimally for the length of all feasible chains, rather than just greedily choosing the first pair.

Let's check out what happens if we sort the above list of pairs now using the second element. The above example would be changed to`[2, 4], [5, 8], [1, 10], [9, 11]`. If we begin by greedily choosing the pairs, we will choose`[2, 4], [5, 8], [9, 11]`, yielding the answer`3`, which is the right answer.

Will this always work?

Consider`pairA`and`pairB`, where`pairA`appears before`pairB`in the sorted pairs based on the second element. We want to figure out if it is always correct to pick`pairA`first if it comes before any other pair`pairB`.

Since`pairA`comes before`pairB`in the sorted list, it implies that`pairA[1] <= pairB[1]`. There are no guarantees on`pairA[0]`and`pairB[0]`.

Now, if`pairA[1] < pairB[0]`, it's obvious that we should append`pairA`first. This is because after picking`pairA`we can still pick`pairB`.

When`pairA[1] >= pairB[0]`, we have to choose carefully. It means that either we only append`pairA`to the chain, or we only append`pairB`to the chain. Appending either`pairA`or`pairB`will increment the length of the chain by`1`but will affect the next pair we can pick.

The tail of the current chain would be`pairA[1]`if we choose`pairA`and would be`pairB[1]`if choose`pairB`. Since`pairA[1] < pairB[1]`(due to sorting), it is better to choose`pairA`first because that way we expose a smaller tail which has a better opportunity to append more future pairs.

As you can see, in both cases, it is better to pick`pairA`. So, this greedy approach of sorting`pairs`based on the second element and then greedily picking pairs whenever we can starting from the first pair will always give the length of the longest chain.