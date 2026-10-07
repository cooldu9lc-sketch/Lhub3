### Further Thoughts: The Best of Both Worlds

> Below is some additional discussion on how the algorithms we have created can be combined to create a fully optimized approach. The previous solutions would be sufficient in an interview setting; this is just bonus content.

Approach 3 has a time complexity of*O*(*N*+*k*). Approach 4 has a time complexity of*O*(*N*⋅*l**o**g*(*N*)). When`k`is large compared to`N`, approach 4 is faster. When`N`is not large compared to`k`, such as in the example`nums = [1, 2, 3, 4, ..., 9997, 9998, 9999]`, we should use approach 3.

It should be noted that the time complexity*O*(*N*⋅*l**o**g*(*N*))is for the worst case. We are actually only sorting the number of keys in`points`, which is equal to the number of unique elements in`nums`. When we precompute`points`, we can find the number of keys`n`as well as`k`. With`n`and`k`, we can decide if approach 3 or approach 4 is faster, and then perform the faster one.

For approach 3, we iterate`k = maxNumber`times. For approach 4, we iterate`n`times after performing`n * log(n)`operations to sort. If`k < n + n * log(n)`, then it is better to use the algorithm from approach 3. Otherwise, it might be more efficient to use the algorithm from approach 4.