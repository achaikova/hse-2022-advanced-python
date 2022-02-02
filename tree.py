import _ast
import ast

import networkx as nx


class ASTplot(ast.NodeVisitor):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.parents_stack = []
        self.operations = [_ast.Add, _ast.Mult, _ast.Sub, _ast.USub]
        self.color_map = {'Module': "#2E86C1", 'FunctionDef': "#1ABC9C", 'Assign': "#F1C40F", 'For': "#F5B041",
                          'If': "#E67E22", 'Num': "#C0392B", 'Operation': "#585da0", 'Name': "#de4c10",
                          'BinOp': "#de1010", 'LtE': "#884EA0", 'Compare': "#7b46df", 'args': "#E74C3C",
                          'Subscript': "#229954",
                          'Index': "#28B463", 'UnaryOp': "#5D6D7E"}

    def generic_visit(self, node):
        parent_node = None
        if len(self.parents_stack) > 0:
            parent_node = self.parents_stack[-1]
        self.parents_stack.append(hash(node))
        if type(node) in self.operations:
            child_node = hash(hash(node) + parent_node)
        else:
            child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['Operation'],
                            style='filled')
        if parent_node is not None:
            self.graph.add_edge(parent_node, child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_Module(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['Module'],
                            style='filled')
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_FunctionDef(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect',
                            fillcolor=self.color_map['FunctionDef'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_Assign(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect',
                            fillcolor=self.color_map['Assign'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_arg(self, node):
        self.graph.add_node(node.arg, shape='rect', fillcolor=self.color_map['args'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], node.arg)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_If(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['If'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_Name(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=f"{type(node).__name__} : {node.id}", shape='rect',
                            fillcolor=self.color_map['Name'], style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Load(self, node):
        pass

    def visit_Store(self, node):
        pass

    def visit_Num(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=f"Num={node.n}", shape='rect', fillcolor=self.color_map['Num'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_LtE(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label="<=", shape='rect', fillcolor=self.color_map['LtE'], style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Compare(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['Compare'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_For(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['For'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_For(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['For'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_UnaryOp(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['UnaryOp'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_BinOp(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['BinOp'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_Subscript(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['Subscript'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()

    def visit_Index(self, node):
        child_node = hash(node)
        self.graph.add_node(child_node, label=type(node).__name__, shape='rect', fillcolor=self.color_map['Index'],
                            style='filled')
        self.graph.add_edge(self.parents_stack[-1], child_node)
        self.parents_stack.append(child_node)
        ast.NodeVisitor.generic_visit(self, node)
        self.parents_stack.pop()
