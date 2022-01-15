class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
    def insert_end(data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.last = node
        else:
            node.prev = self.last
            self.last = node
    def delete_end():
        if self.head == None:
            return
        else:
            self.last = self.last.prev
