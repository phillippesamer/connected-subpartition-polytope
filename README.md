# Connected subpartition polytope facets
Tools for inspecting facets of the connected k partition polytope of a graph: the convex hull of characteristic vectors of disjoint vertex subsets inducing k connected subgraphs.

### Dependencies

We use [polymake](https://polymake.org) and python3.8, with the networkx library.

### How to use this

To enumerate the facets of the polytope _P(G,k)_, one should

- add a function on `connected_subpartition_polytope.py` to create the desired input graph _G_ (just mimic one of the examples in the beginning, _e.g._ `get_graph_P5()`)
- edit the first lines of the `main()` function to set the number of colours _k_, and desired output file paths
- run `python3.8 connected_subpartition_polytope.py`

Have fun! (:
