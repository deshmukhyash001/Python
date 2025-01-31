#Doubly Linked List

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LL():
    def __init__(self):
        self.head = None

    def push(self,newval):
        NewVal = Node(newval)
        if not self.head:
            self.head = NewVal
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = NewVal
        NewVal.prev = last_node

    def Display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = " -> ")
            current_node = current_node.next
        print("Null")

    def Display_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        
        while current_node:
            print(current_node.data, end = " -> " )
            current_node = current_node.prev
        print("Null")

DLL = Doubly_LL()
DLL.push(5)
DLL.push(10)
DLL.push(15)
DLL.push(20)
DLL.Display_forward()
DLL.Display_backward()

