class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def search(self,data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def calculate_sum(self):
        sum = 0

        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()

        return sum
    
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    bin_tree = build_tree([15,12,27,7,14,20,88,23])
    print(bin_tree.in_order_traversal())
    print(bin_tree.pre_order_traversal())
    print(bin_tree.post_order_traversal())

    print(f"Min is {bin_tree.find_min()}")
    print(f"Max is {bin_tree.find_max()}")
    print(f"Sum is {bin_tree.calculate_sum()}")
    
    
    
    
   
