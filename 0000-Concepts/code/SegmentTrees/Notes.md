Template 1 — Point update + range query

Template 2 — Range add + point query

Template 3 — Lazy propagation


For lazy propagation, rather than trying to memorize a single magical implementation, memorize these four responsibilities:

apply(node, update)


push(node)


pull(node)


query/update interval

and then ask:

1. What does tree[node] mean?
2. What does lazy[node] mean?
3. How does an update affect an entire segment?
4. If combining children, what is combine()?
5. Do I need segment length?
6. How do lazy updates compose?