import ast
import astunparse
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
    
file = open(filename, "r")
tree = ast.parse(file.read())
print(ast.dump(tree, indent=4))

def splitTree(tree, parent):
    export = []
    for item in tree:
        itemType = str(item.__class__).split("'")[1].split(".")[1]
        if itemType == 'Assign':
            export.append(codeItem('assign', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == 'Expr':
            export.append(codeItem('expr', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == "While":
            c = codeItem('while', astunparse.unparse(item), item, -1, -1, parent, -1)
            c.body = splitTree(item.body, c.id)
            c.orelse = splitTree(item.orelse, c.id)
            export.append(c)
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
        elif item.variant == 'while':
            export += f'<div class="whileWrapper"><div class="while" id="{item.id}" data-parent="{item.parent}">{item.content.split(":")[0]}\n</div>\n\n' 
            export += printTree(item.body)
            export += '</div>\n\n'
#            export += printTree(item.orelse)
        elif item.variant == 'if':
            export += f'<div class="ifWrapper">\n\n<div class="if" id="{item.id}" data-parent="{item.parent}">{item.content.split(":")[0]}\n</div>\n\n'
            export += printTree(item.body)
            export += '</div>\n\n'
            export += printTree(item.orelse)
            
    
    return export

html += printTree(finTree)

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