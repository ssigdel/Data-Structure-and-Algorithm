class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def create_tree(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if current.data > val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)

                elif current.data < val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                else:
                    break
    
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)


if __name__ == '__main__':
    bst = BinarySearchTree()
    arr = [5, 1, 3, 4, 2]
    for i in arr:
        bst.create_tree(i)
    print("Preorder:")
    preOrder(bst.root)
    print("Inorder:")
    inOrder(bst.root)
    print("Postorder:")
    postOrder(bst.root)


