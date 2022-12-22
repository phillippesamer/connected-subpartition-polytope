#!/usr/bin/env python3.8
# coding: utf-8

from separators import min_ab_separators

import networkx as nx
import subprocess

def get_graph_P5() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,6))
    G.add_edges_from([(1,2), (2,3), (3,4), (4,5)])
    return G

def get_graph_C4() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,5))
    G.add_edges_from([(1,2), (2,3), (3,4), (4,1)])
    return G

def get_graph_claw() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,5))
    G.add_edges_from([(1,3), (2,3), (3,4)])
    return G

def get_graph_paw() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,5))
    G.add_edges_from([(1,2), (1,3), (2,3), (3,4)])
    return G

def get_graph_diamond() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,5))
    G.add_edges_from([(1,2), (1,3), (1,4), (2,3), (3,4)])
    return G

def get_graph_k_1_4() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,6))
    G.add_edges_from([(1,2), (1,3), (1,4), (1,5)])
    return G

def get_graph_k_1_5() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,7))
    G.add_edges_from([(1,2), (1,3), (1,4), (1,5), (1,6)])
    return G

def get_ilp_formulation(G: nx.Graph, k: int) -> str:
    """
    Create a string representing the .lp file for the 
    "separators formulation" of connected subpartition
    of G into k connected subgraphs
    """
    n = G.number_of_nodes()
    m = G.number_of_edges()

    # strings corresponding to variable names
    vars = {}
    for u in range(1,n+1):
        for c in range(1, k+1):
            vars[(u,c)] = " x" + str(u) + "," + str(c) + " "

    # objective function: arbitrary coefficients
    objective = "Maximize\n  "
    for u in range(1,n+1):
        objective += str(u * ((u-1)%k+1))
        objective += vars[(u,(u-1)%k+1)]
        if u < n:
            objective += "+ "
        else:
            objective += "\n"

    constraints = "Subject To\n"
    # first class of constraints: 1 colour bound for each vertex
    for u in range(1,n+1):
        constraints += "GUB" + str(u) + ":"
        for c in range(1,k+1):
            constraints += vars[u,c]
            if c < k:
                constraints += "+"
        constraints += "<= 1\n"
    # second class of constraints: separator inequalities
    for u in range(1,n+1):
        for v in range(u+1, n+1):
            if (G.has_edge(u,v) == False):
                print("sep("+str(u)+","+str(v)+")")
                separators = min_ab_separators(G,u,v)
                for idx,Z in enumerate(separators):
                    for c in range(1,k+1):
                        #label
                        constraints += "(" + str(u) + "," + str(v) + ")-SEP_"
                        constraints += "#" + str(idx+1) + "_c" + str(c) + ":"
                        #x_u,c + x_v,c - \sum_(z in Z) x_z,c <= 1
                        constraints += vars[u,c] + "+" + vars[v,c]
                        for z in Z:
                            constraints += "-" + vars[z,c] 
                        constraints += "<= 1\n"

    # not applicable in this formulation
    bounds = "Bounds\n"

    domain = "Binaries\n"
    for u in range(1,n+1):
        for c in range(1,k+1):
            domain += vars[u,c]
    domain += "\n"
 
    sections = [objective, constraints, bounds, domain, "End\n"]
    contents = "\n".join(sections)
    return contents

def main():
    # input graph and number of colours (connected subgraphs)
    graph = get_graph_claw()
    colours = 3
    output_lp_file     = "examples/g=claw_and_k=3_original.lp"
    output_facets_file = "examples/g=claw_and_k=3_facets.lp"

    # generate "separators formulation" ilp corresponding to this input
    print("writing ilp on file " + output_lp_file)

    ilp = get_ilp_formulation(graph,colours)

    f = open(output_lp_file, 'w')
    f.write(ilp)
    f.close()

    print("done\n")

    # run polymake to enumerate facets of the corresponding convex hull
    print("running polymake and writing facets on file " + output_facets_file)

    proc = subprocess.run(
    ["polymake", "--script", "polymake_cvxhull_from_lp.pl", output_lp_file],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

    f = open(output_facets_file, 'w')
    f.write(proc.stdout)
    f.close()

    print(proc.stderr)
    print("done\n")


if __name__ == "__main__":
    main()
