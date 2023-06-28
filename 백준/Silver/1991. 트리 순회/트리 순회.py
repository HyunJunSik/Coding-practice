class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre(Node):
    print(Node.data,end='')
    if Node.left != '.':
        pre(t[Node.left])
    if Node.right != '.':
        pre(t[Node.right])
        
def inorder(Node):
    if Node.left != '.':
        inorder(t[Node.left])
    print(Node.data,end='')
    if Node.right != '.':
        inorder(t[Node.right])
        
def post(Node):
    if Node.left != '.':
        post(t[Node.left])
    if Node.right != '.':
        post(t[Node.right])  
    print(Node.data,end='') 

t = {}
for i in range(int(input())):
    data, left, right = map(str, input().split())
    t[data] = Node(data, left, right)

pre(t['A'])
print()
inorder(t['A'])
print()
post(t['A'])
print()
