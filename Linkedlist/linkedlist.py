#node class having data and pointer to next node
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#linkedlist class for actual implementation
class Linkedlist:
    #constructor: creates head node
    def __init__(self):
        self.head = None

    #inserts node at the beginning of the linked list
    def insert_at_first(self, data):
        node = Node(data, self.head)
        self.head = node

    #inserts node at the end of the linked list
    #checks if the node is empty, if so, insert data at head node
    #otherwise iterate through the node and insert new node when next node is none.
    def insert_at_last(self, data):
        if self.head is None:  
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    #take a list as input and creates node by iteration
    #if the head is none start inserting data from the head
    #otherwise insert at the first of the existing list
    def insert_list(self, list_data):
        if self.head is None:
            for i in list_data:
                self.head = Node(i, self.head)
            return
        
        for i in list_data:
            self.insert_at_first(i)

    #take an index and element to insert 
    def insert_index(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_first(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next


    #take the index and remove the element
    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next #assign head -> next to next of node to be removed
                break
            itr = itr.next
            count += 1
    
    def remove_by_value(self, data):
        itr = self.head
        pre = None
        while itr:
            if itr.data == data:
                pre.next = itr.next
                break
            pre = itr
            itr = itr.next
        
    #function to get the length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    #helper function to print the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        liststr = ''

        while itr:
            liststr += str(itr.data) + ' --> '
            itr = itr.next
        print('\n', liststr)

#driver function
if __name__ == '__main__':
    ll = Linkedlist()
    data = [1, 2, 3, 4, 5]
    ll.insert_list(data)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.insert_at_first(10)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.insert_at_last(20)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.remove(2)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.insert_index(6, 1)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.insert_after_value(3, 4)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
    ll.remove_by_value(5)
    ll.print()
    print("\n Length of linked list is: ", ll.get_length())
