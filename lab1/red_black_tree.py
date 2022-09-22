import sys

from color import Color


class Node:
    def __init__(self, data):
        self.data = data
        self.color = Color.red
        self.parent = None
        self.left = None
        self.right = None


class RedBlack_tree:
    def __init__(self):
        self.nil = Node(Color.black)
        self.nil.color = Color.black
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def transplant(self, parent, child):
        if parent.parent is None:
            self.root = child
        elif parent is parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        child.parent = parent.parent

    def added_node(self, color, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.nil
        node.right = self.nil
        node.color = color

        y = None
        x = self.root

        while x is not self.nil:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        if node.parent is None:
            node.color = Color.black
            return
        if node.parent.parent is None:
            return

    def left_rotate(self, x, y):      #-> x-father; y - child
        x.right = y.left
        y.left = x
        x.parent = y

        if y.left is not self.nil:
            y.parent.left = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y


    def right_rotate(self, x, y):       #-> x-father; y - child
        x.left = y.right
        y.right = x
        x.parent = y

        if y.right is not self.nil:
            y.parent.right = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y


    def fix_colors(self, current):
        while current is not self.root and current.color is Color.black:
            if current is current.parent.left:
                sibling = current.parent.right

                # case 3.1
                if current.parent.right.color is Color.red:
                    sibling.color = Color.black
                    current.parent.color = Color.red
                    self.left_rotate(current.parent)

                # case 3.2
                elif sibling.left.color is Color.black and sibling.right.color is Color.black:
                    sibling.color = Color.red
                    current = current.parent

                # case 3.3
                elif sibling.right.color is Color.black:
                    sibling.left.color = Color.black
                    sibling.color = Color.red
                    self.right_rotate(sibling)

                # case 3.4
                else:
                    sibling.color = current.parent.color
                    current.parent.color = Color.black
                    sibling.right.color = Color.black
                    self.left_rotate(current.parent)
                    self.root = current
            else:
                sibling = current.parent.left

                # case 3.1
                if sibling.color is Color.red:
                    sibling.color = Color.black
                    current.parent.color = Color.red
                    self.right_rotate(current.parent)

                # case 3.2
                elif sibling.left.color is Color.black and sibling.right.color is Color.black:
                    sibling.color = Color.red
                    current = current.parent

                # case 3.3
                elif sibling.left.color is Color.black:
                    sibling.right.color = Color.black
                    sibling.color = Color.red
                    self.left_rotate(sibling)

                # case 3.4
                else:
                    sibling.color = current.parent.color
                    current.parent.color = Color.black
                    sibling.left.color = Color.black
                    self.right_rotate(current.parent)
                    self.root = current

        current.color = Color.black

    def delete_node(self, node, key):
        del_node = self.nil
        while node is not self.nil:
            if node.data is key:
                del_node = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if del_node is self.nil:
            print("no node found")
            return

        y = del_node
        y_original_color = y.color
        if del_node.left is self.nil:
            current = del_node.right
            self.transplant(del_node, del_node.right)
        elif del_node.right is self.nil:
            current = del_node.left
            self.transplant(del_node, del_node.left)
        else:
            current = y.right
            if y.parent is del_node:
                current.parent = y
            else:
                self.transplant(y, y.right)
                y.parent.right = y
            self.transplant(del_node, y)
            y.parent.left = y
            y.color = del_node.color
        if y_original_color is Color.black:
            self.fix_colors(current)

    def print_tree(self, node, indent, last):
        if node is not self.nil:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "        "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color is Color.red else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

    def RBT_delete_node(self, data):
        self.delete_node(self.root, data)

    def print(self):
        self.print_tree(self.root, "", True)


rbt = RedBlack_tree()

rbt.added_node(Color.black, 30)
rbt.added_node(Color.black, 50)
rbt.added_node(Color.red, 18)
rbt.added_node(Color.black, 20)
rbt.added_node(Color.black, 13)
rbt.added_node(Color.red, 15)
rbt.added_node(Color.red, 12)

rbt.print()
rbt.RBT_delete_node(12)
print("\n\n")
rbt.print()
