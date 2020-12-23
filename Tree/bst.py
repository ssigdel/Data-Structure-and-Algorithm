class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    #add new child node  
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
                
                
     # inorder traversal: left, root, right     
    def inorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversal()
         
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder_traversal()
         
        return elements
        
     # preorder traversal: root, left, right
    def preorder_traversal(self):
        elements = []
     
        elements.append(self.data)
     
        if self.left:
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements += self.right.preorder_traversal()
        
        return elements
        
     # postorder traversal: left, right, root 
    def postorder_traversal(self):
        elements = []
     
        if self.left:
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements += self.right.preorder_traversal()
            
        elements.append(self.data)
        
        return elements
        
    # search a given value in the tree.
    def search(self, value):
        if self.data == value:
            return True
    
        if self.data > value:
            if self.left:
                return self.left.search(value)
            
            else:
                return False
            
        if self.data < value:
            if self.right:
                return self.right.search(value)
                
            else:
                return False

    # calculate sum of elements in the tree
    def calculate_sum(self):
        sum = 0

        if self.data:
            if self.left:
                sum += self.left.calculate_sum() 

            if self.right:
                sum += self.right.calculate_sum()

            sum += self.data

        return sum

    # smallest element in the tree  
    def smallest(self):
        if self.left:
            return self.left.smallest()
        else:
            return self.data
            
    # greatest element in the tree       
    def greatest(self):
        if self.right:
            return self.right.greatest()
            
        else:
            return self.data
                      
# helper function to build the tree
def build_tree(data):
    root = BSTNode(data[0])
    
    for i in range(1, len(data)):
        root.add_child(data[i])
    
    return root
 
# driver function   
if __name__ == "__main__":
    data = [5, 3, 1, 2, 6, 7, 10]
    root = build_tree(data)

    print("\n Inorder traversal:")
    print(root.inorder_traversal())

    print("\n Preorder traversal:")
    print(root.preorder_traversal())

    print("\n Postorder traversal:")
    print(root.postorder_traversal())

    print("\n Smallest element is:")
    print(root.smallest())

    print("\n Largest element is:")
    print(root.greatest())

    result = root.search(9)
    if result:
        print("\n Element found")
    else:
        print("\n Element not found")

    print("\n Sum of given elements is:")
    print(root.calculate_sum())
             