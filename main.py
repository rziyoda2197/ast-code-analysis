import ast

def hisobla_for_sikl(kod):
    tree = ast.parse(kod)
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            return len(node.orelse) + len(node.body)
    return 0

kod = """
for i in range(10):
    for j in range(10):
        print(i, j)
"""

print(hisobla_for_sikl(kod))
