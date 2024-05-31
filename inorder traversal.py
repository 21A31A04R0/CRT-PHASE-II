class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
 
 
def printInorder(root):
    if root == None:
        return 
    # 1 
    printInorder(root.left)
    # 2 
    print(root.data, end = ", ")
    # 3
    printInorder(root.right)

 
#      12 
#     5  8 
#   -1 2   89
obj1 = Node(12)
obj2 = Node(5)
obj3 = Node(8)
obj4 = Node(-1)
obj5 = Node(2)
obj6 = Node(89)
obj1.left = obj2
obj1.right = obj3 
obj2.left = obj4
obj2.right = obj5
obj3.right = obj6
 
printInorder(obj1)
print()
 
 
 
 
 
 
 
 
 
