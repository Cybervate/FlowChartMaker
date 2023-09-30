class codeItem:

    def __init__(self, variant, content, node, body, orelse, parent, child):
        self.id = id(self)
        self.variant = variant
        self.content = content
        self.node = node
        self.body = body
        self.orelse = orelse
        self.parent = parent
        self.child = child
