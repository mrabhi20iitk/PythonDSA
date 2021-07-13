#Linked list

#creating a node
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#creating a Linked List
class Linked_list:
    def __init__(self):
        self.head = None

    #adding a element in beginning
    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #inserting at end
    def insertAtEnd(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    #deleting a node
    def DeleteNode(self,position):
        if self.head is None:
            print('empty?')
            return

        temp = self.head

        if position==0:
            temp = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            print('index out of range?')
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    #printing a linked list
    def printllist(self):
        temp = self.head
        while temp:
            print(str(temp.data)+' ',end='')
            temp = temp.next

if __name__ == '__main__':
    ll = Linked_list()
    ll.insertAtBeginning(5)

    ll.DeleteNode(3)
    print('')
    ll.printllist()







