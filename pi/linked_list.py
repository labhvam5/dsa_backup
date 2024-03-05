class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = None
        mover = self.head
        while mover.next != None:
            mover = mover.next

        mover.next = new_node
        return
    
    def print_values(self):
        mover = self.head
        while mover != None:
            print(mover.data)
            mover = mover.next

li = Linked_list()
li.insert_at_end(1)
li.insert_at_end(2)
li.insert_at_end(3)
li.print_values()