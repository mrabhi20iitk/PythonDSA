#Binary Tree

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:   #check for left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        if data > self.data:  # check for left sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

            #In-order Traversal
    def in_order_traversal(self):         # left --> root --> right
        elem = []

        if self.left:
            elem += self.left.in_order_traversal()

        elem.append(self.data)

        if self.right:
            elem+= self.right.in_order_traversal()


        return elem

    # In-order Traversal
    def pre_order_traversal(self):
        temp = []
        temp.append(self.data)
        if self.left:
            temp += self.left.pre_order_traversal()

        if self.right:
            temp += self.right.pre_order_traversal()

        return temp

    # In-order Traversal
    def post_order_traversal(self):
        temp = []
        if self.left:
            temp += self.left.post_order_traversal()
        if self.right:
            temp += self.right.post_order_traversal()

        temp.append(self.data)

        return temp

#searching an element
    def search(self,val):
        if val == self.data:
            return True

        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # finding the max value in tree
    def findmax(self):
        if self.right:
            return self.right.findmax()
        else:
            return self.data

    #finding the min value in sub tree
    def findmin(self):
        if self.left:
            return self.left.findmin()
        else:
            return self.data

    #deleting a node by right tree min method
    def delete(self,val):
        if val< self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right =  self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.findmin()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    ele = [17,4,1,20,9,23,34]
    b = build_tree(ele)
    b.add_child(18)
    print(b.in_order_traversal())
    print(b.pre_order_traversal())
    print(b.post_order_traversal())
    print(b.search(20))
    print(b.search(21))
    print(b.findmax())
    print(b.findmin())
    b.delete(9)
    print(b.in_order_traversal())






