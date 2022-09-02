#There are some mistakes in his code and this is what I want you to learn.

# implent linked list  
class Node :
    def __init__(self,data=None,next=None):
        self.data = data;
        self.next = next;

  


# linkedlist
class LinkedList: 
    def __init__(self,nodes):
        if nodes is not None:
            # There is some change here
         self.head = nodes.pop(0);
        for item in nodes:
            self.next = item;   

    def head1(self):
        # we should get  a head that we will pass in  as an argument.
        return self.head        

    def next1(self):
         return self.next; 

# trying inserting a node at the first position
    def insert_first(self,node):
        self.head = node;
        return self.head; 

    def insert_last(self,node):
       if self.head is  None:
            self.head = node
            return "Nothing was found to be the head"; 
       for current_item in self:
                NewNode = current_item;  
                return NewNode;


    def all(self):
        nodes = [self.head,self.next];
        return "->".join(nodes);
       #This makes the linkedlist iterable.
    def __iter__(self):
        node = self.head  
        while node is not None:
          yield node
          node = node.next; 
 
fnode = ['Samuel','Akinie'];
fLinkedList  = LinkedList(fnode );
print(f"{fLinkedList.head1()}");
print(f"{fLinkedList.next1()}");
print(f"{fLinkedList.insert_first('menzgold')}");
print(f"{fLinkedList.insert_last('simon')}");
print(f"{fLinkedList.all()}");