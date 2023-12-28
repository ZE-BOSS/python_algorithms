class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    iPhone = TreeNode("iPhone")
    iPhone.add_child(TreeNode("iPhone_12"))
    iPhone.add_child(TreeNode("iPhone_7"))
    iPhone.add_child(TreeNode("iPhone_15"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(iPhone)
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    print({"data": root.data, "children": root.children, "parent": root.parent})
    print({"data": laptop.data, "children": laptop.children, "parent": laptop.parent})
    print({"data": cellphone.data, "children": cellphone.children, "parent": cellphone.parent})
    print({"data": tv.data, "children": tv.children, "parent": tv.parent})
    print({"data": iPhone.data, "children": iPhone.children, "parent": iPhone.parent})

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()