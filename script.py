import ast

filename = "ExampleCode.py"

# with open(filename) as f:
#     tree = ast.parse(f.read(), filename=filename)

# print(tree)

# for node in ast.walk(tree):
#     print(node)
#     print(node.__dict__)
#     print("children: " + str([x for x in ast.iter_child_nodes(node)]) + "\\n")
from redbaron import RedBaron
file = open(filename, "r")
red = RedBaron(file.read())
print(red.int_)