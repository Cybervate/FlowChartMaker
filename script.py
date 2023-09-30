import ast
import astunparse
from redbaron import RedBaron
#from bs4 import BeautifulSoup as Soup
from collections import deque
from obs import codeItem

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

# def assign(code, node):
#     global html
#     global finTree
#     #html += f'<div class="assign">{code}</div>\n\n'
#     finTree.append(codeItem('assign', astunparse.unparse(node), node, 1, 2))

# def exprFunc(code, node):
#     global html
#     global finTree
#     #html += f'<div class="expr">{code}</div>\n\n'
#     finTree.append(codeItem('expr', astunparse.unparse(node), node, 1, 2))

# def ifFunc(code, node):
#     global html
#     global finTree
#     #html += f'<div class="if">{code}</div>\n\n'
#     finTree.append(codeItem('if', astunparse.unparse(node), node, 1, 2))

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
        info = f"{node.targets[0].id} = {node.value.value}"
        #print(f"Assign: {info}")
        assign(info, node)

    def visit_Expr(self, node):
        info = f'{node.value.func.id}({node.value.args[0].id})'
        #print(f'Expr: {info}')
        exprFunc(info, node)

    def visit_If(self, node):
        info = f'If {node.test.left.id} {str(node.test.ops[0].__class__).split(".")[-1][:-2]} {node.test.comparators[0].value}:'
        #print(info)
        ifFunc(info, node)
        
        #print("THEN")
        ast.NodeVisitor.visit(self, node.body[0])
        #print("ENDTHEN")

        #print('ELSE')
        ast.NodeVisitor.visit(self, node.orelse[0])
        #print('ENDELSE')
    
file = open(filename, "r")
tree = ast.parse(file.read())
v = Visitor()
print(ast.dump(tree, indent=4))

def SplitTreeFunc(tree):
    pass

def splitTree(tree, parent):
    export = []
    for item in tree:
        itemType = str(item.__class__).split("'")[1].split(".")[1]
        if itemType == 'Assign':
            export.append(codeItem('assign', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == 'Expr':
            export.append(codeItem('expr', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == 'If':
            c = codeItem('if', astunparse.unparse(item), item, -1, -1, parent, -1)
            c.body = splitTree(item.body, c.id)
            c.orelse = splitTree(item.orelse, c.id)
            export.append(c)
    return export

finTree = splitTree(tree.body, -1)

def printTree(tree):
    export = ""
    for item in tree:
        print(f'X: {item.orelse}, Y: {item.id}')

        if item.variant == 'assign':
            export += f'<div class="assign" id="{item.id}" data-parent="{item.parent}">{item.content}</div>\n\n'
        elif item.variant == 'expr':
            export += f'<div class="expr" id="{item.id}" data-parent="{item.parent}">{item.content}</div>\n\n'
        elif item.variant == 'if':
            export += f'<div class="ifWrapper">\n\n<div class="if" id="{item.id}" data-parent="{item.parent}">{item.content.split(":")[0]}\n</div>\n\n'
            export += printTree(item.body)
            export += '</div>\n\n'
            export += printTree(item.orelse)
            
    
    return export

html += printTree(finTree)

#for node in walk(tree):
#    v.visit(node)

# for item in finTree:
#     print(f'Variant: {item.variant}, Content: {item.content}')
#     if item.variant == 'assign':
#         html += f'<div class="assign">{item.content}</div>\n\n'
#     elif item.variant == 'expr':
#         html += f'<div class="expr">{item.content}</div>\n\n'
#     elif item.variant == 'if':
#         html += f'<div class="if">{item.content.split(":")[0]}</div>\n\n'

html += """
        </div>
        <div class="end" id="end">End</div>
    </body>
</html>"""

print(finTree)
for item in finTree:
    print(f'Variant: {item.variant}, Content: {item.content}')
    if item.variant == "if":
        for j in item.orelse:
            print(f'\tVariant: {j.variant}, Content: {j.content}')

f = open("flowchart.html", "w")
f.write(html)
f.close()