import ast
import os

import tree
import networkx as nx


def main():
    with open('fibonacci.py', 'r') as f:
        fibonacci_tree = ast.parse(f.read())
    dot_tree = tree.ASTplot()
    dot_tree.visit(fibonacci_tree)
    if not os.path.exists(artifacts_dir):
        os.makedirs(artifacts_dir)
    nx.drawing.nx_pydot.to_pydot(dot_tree.graph).write_png(f'{artifacts_dir}/ast_tree.png')


if __name__ == '__main__':
    artifacts_dir = 'artifacts/'
    main()
