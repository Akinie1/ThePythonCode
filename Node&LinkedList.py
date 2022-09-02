# create a node 
class Node:
    def __init__(self,data,next):
        self.data = data;
        self.next = next;
    def get_next(self):
        return self.next;    
    def get_data(self):
        return self.data
    def __repr__(self):
       return self.data


# creating an instance of the class Node

# fnode = Node("Akinie","None")
# print(f"{fnode}");

# creating a linkedlist.
class LinkedList :
      def __init__(self,data):
        self.head = data.data
        self.next = data.next;

      def __repr__(self):
          node = self.head;
          tail = self.next;
          nodes = [];
          nodes.append(node);
          nodes.append(tail);
          nodes.append("menzgold");
          return "->".join(nodes)



 #creating an instance of a class   
fnode = Node("Samuel(head)","Akinie(tail)");
linkedList = LinkedList(fnode);
print(f"{linkedList}");

