import ast
from redbaron import RedBaron
#from bs4 import BeautifulSoup as Soup
from collections import deque

def walk(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if isinstance(node, tuple):
            queue.extend(node[1:])  # add the children to the queue
        yield node

html = ''
with open('import.html', "r") as h:
    html = h.read()

filename = "ExampleCode.py"

def addArrow(text):
    return f'\n<div class="arrow">|<br>|<br>{text}<br>|<br>|<br>V</div>\n\n'

def assign(code):
    return f'<div class="assign">{code}</div>\n\n'

def exprFunc(code):
    return f'<div class="expr">{code}</div>\n\n'

def ifFunc(code):
    return f'<div class="if">{code}</div>\n\n'

class Visitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        print(f'Name: {node.id}')
        pass

    def visit_Num(self, node):
        print(f'Num: {node.__dict__["value"]}')

    def visit_Str(self, node):
        print(f'Str: {node.s}')

    def visit_Print(self, node):
        print("Print: ")

    def visit_Assign(self, node):
        global html
        info = f"{node.targets[0].id} = {node.value.value}"
        print(f"Assign: {info}")
        html += assign(info)

    def visit_Expr(self, node):
        global html
        info = f'{node.value.func.id}({node.value.args[0].id})'
        print(f'Expr: {info}')
        html += exprFunc(info)

    def visit_If(self, node):
        global html
        info = f'If {node.test.left.id} {str(node.test.ops[0].__class__).split(".")[-1][:-2]} {node.test.comparators[0].value}:'
        print(info)
        html += ifFunc(info)
        
        print("THEN")
        ast.NodeVisitor.visit(self, node.body[0])
        print("ENDTHEN")

        print('ELSE')
        ast.NodeVisitor.visit(self, node.orelse[0])
        print('ENDELSE')
    
file = open(filename, "r")
tree = ast.parse(file.read())
v = Visitor()
print(ast.dump(tree, indent=4))

html += addArrow('')

for node in walk(tree):
    v.visit(node)

html += """
        </div>
        <div class="end">End</div>
    </body>
</html>"""

f = open("flowchart.html", "w")
f.write(html)
f.close()