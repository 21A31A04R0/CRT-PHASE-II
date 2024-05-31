class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
def printRightView(root):
     if root == None:
        return 
     Q = [root]
     result = []
     while len(Q) > 0:
         n = len(Q)
         for i in range(n):
             # step-1 (Deleting)
             currNode = Q.pop(0)
 
             # step-2 (Appending to result)
             if i == n - 1:
                 result.append(currNode.data)
 
             # step-3 (Enquing the left child)
             if currNode.left != None:
                 Q.append(currNode.left)
 
             # step-4 (Enquing the right child)
             if currNode.right != None:
                 Q.append(currNode.right)
 
     print("Right view is:", result)
 
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
printRightView(obj1)
 
