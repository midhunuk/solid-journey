class Node:
    def __init__(self, v, next = None):
        self.v = v
        self.next = next
    def isEmpty(self):
        return self.next == None

def reverse(root):
    if root.isEmpty():
        return root
    currentNode = root.next
    root.next = None
    previousNode = root
    while(currentNode != None):
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

v = reverse(n1)
print("hi")