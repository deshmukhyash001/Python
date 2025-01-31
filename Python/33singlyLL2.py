class Node:
    def __init__(self,data=None):
        self.data=data
        self.next =None
class slinked_list:
    def __init__(self):
        self.head=None
    def printlist(self):
        printval=self.head
        while printval is not None:
            print(printval.data,end=' -> ')
            printval = printval.next
        print("Null")
list=slinked_list()
list.head=Node('mon')
e2=Node('tue')
e3=Node('wed')

list.head.next=e2
e2.next=e3

list.printlist()


