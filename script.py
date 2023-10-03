import ast
import astunparse
from obs import codeItem
import sys

def splitTree(tree, parent, elseQ):
    export = []
    for item in tree:
        itemType = str(item.__class__).split("'")[1].split(".")[1]
        if itemType == 'Assign' or itemType == 'AugAssign':
            export.append(codeItem('assign', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == 'Expr':
            export.append(codeItem('expr', astunparse.unparse(item), item, -1, -1, parent, -1))
        elif itemType == "For":
            c = codeItem('for', astunparse.unparse(item), item, -1, -1, parent, -1)
            c.body = splitTree(item.body, c.id, False)
            export.append(c)
        elif itemType == "While":
            c = codeItem('while', astunparse.unparse(item), item, -1, -1, parent, -1)
            c.body = splitTree(item.body, c.id, False)
            c.orelse = splitTree(item.orelse, c.id, False)
            export.append(c)
        elif itemType == 'If':
            if elseQ:
                c = codeItem('elif', astunparse.unparse(item), item, -1, -1, parent, -1)
                c.body = splitTree(item.body, c.id, False)
                c.orelse = splitTree(item.orelse, c.id, True)
                export.append(c)
            else:
                c = codeItem('if', astunparse.unparse(item), item, -1, -1, parent, -1)
                c.body = splitTree(item.body, c.id, False)
                c.orelse = splitTree(item.orelse, c.id, True)
                export.append(c)
    return export

def printTree(tree):
    export = ""
    for item in tree:
        print(f'X: {item.orelse}, Y: {item.id}')

        if item.variant == 'assign':
            export += f'<div class="assign" id="{item.id}" data-parent="{item.parent}">{item.content}</div>\n\n'
        elif item.variant == 'expr':
            export += f'<div class="expr" id="{item.id}" data-parent="{item.parent}">{item.content}</div>\n\n'
        elif item.variant == 'for':
            export += f'<div class="forWrapper"><div class="for" id="{item.id}" data-parent="{item.parent}">{item.content.split(":")[0]}\n</div>\n\n'
            export += printTree(item.body)
            export += '</div>\n\n'
            print(f"TTTTTYYYYYYY: {item.body}")
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

def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1] 
    else:
        filename = "ExampleCode.py"

    if len(sys.argv) > 2:
        importname = sys.argv[2] 
    else:
        importname = "import.html"

    if len(sys.argv) > 3:
        flowname = sys.argv[3] 
    else:
        flowname = "flowchart.html"

    if len(sys.argv)  > 4:
        leadername = sys.argv[4] 
    else:
        leadername = "leader-line.min.js"

    if len(sys.argv)> 5:
        arrowname = sys.argv[5] 
    else:
        arrowname = "arrows.js"

    with open(importname, "r") as h:
        html = h.read()

    file = open(filename, "r")
    tree = ast.parse(file.read())
    print(ast.dump(tree, indent=4))



    finTree = splitTree(tree.body, -1, False)



    html += printTree(finTree)

    with open(arrowname, "r") as h:
        arrow = h.read()

    with open(leadername, "r") as h:
        leader = h.read()

    html += f"""<div class="end" id="end">End</div>
            </div>
        </body>
        <script>{leader}</script>
        <script>{arrow}</script>
    </html>"""

    print(finTree)
    for item in finTree:
        print(f'Variant: {item.variant}, Content: {item.content}')
        if item.variant == "if":
            for j in item.orelse:
                print(f'\tVariant: {j.variant}, Content: {j.content}')

    f = open(flowname, "w")
    f.write(html)
    f.close()

    return html

if __name__ == "__main__":
    main()