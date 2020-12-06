class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class Doubly_linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_last(self, data):
        if self.head is None:  
            self.head = Node(data, None, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_list(self, list_data):
      self.head = None
      for data in list_data:
          self.insert_at_last(data)

    
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        liststr = ''

        while itr:
            liststr += str(itr.data) + ' --> '
            itr = itr.next
        print('\n', liststr)
    
    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.get_last()
        liststr = ''
        while itr:
            liststr += str(itr.data) + ' <-- '
            itr = itr.prev
        print('\n', liststr)


if __name__ == "__main__":
    dll = Doubly_linkedlist()
    data = [1, 2, 3, 4, 5]
    dll.insert_list(data)
    dll.print_forward()
    dll.print_backward()



