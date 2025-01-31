#Linked list example
class Node:
    def __init__(self, data):
        self.data = data  # Store data  # self.data = 5
        self.next = None  # Pointer to the next node (initialized as None)  # self.next = None

class LinkedList:
    def __init__(self):
        self.head = None     # Initialize the head of the list  # self.head = None
    
    def append(self, newval):     # 5
        New_Val = Node(newval)  # Create a new node 
        if not self.head:   # Checking if self.head is None as self.head will be None only for the first append only
            self.head = New_Val  # If list is empty, make new node the head
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = New_Val  # Point the last node to the new node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("NULL")

# Create a linked list and add elements
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(12)

# Display the list
ll.display()
