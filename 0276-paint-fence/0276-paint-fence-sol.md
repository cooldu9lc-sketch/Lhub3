Paint `n` fence posts using `k` colors.

Constraint:

```
No more than 2 adjacent posts can have same color.
```

---

# State Definition

Instead of tracking colors, track relationship with previous post.

States:

```
same = current post has same color as previous

diff = current post has different color than previous
```

---

# State Diagram

```
          choose same color
diff -----------------> same

          choose different color
same -----------------> diff
diff -----------------> diff
```

Notice:

```
same -> same
```

is illegal because that creates 3 equal colors.

---

# Transition

Suppose we're placing post i.

### Make current same

Only possible if previous state was diff.

```
new_same=diff
```

---

### Make current different

Choose any color except previous color.

```
new_diff= (same+diff) * (k-1)
```