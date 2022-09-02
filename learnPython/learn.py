# create a node 
#Create a linkedList with the functionalities. Try understanding his code.
class Node:

 def __init__(self,data,next):
    self.data = data;
    self.next = next;
 def getData(self):
    return self.data;
 def getNext(self):     
    return self.next;
 def __repr__(self):
    return self.data;

 #creating an instance of the class. 




# learning to create a simple linkedList.
# class LinkedList :

#   def __init__(self,data):
#     self.data = data.data;
#     self.next =data.next

#   def __repr__(self):
#     head = self.data
#     tail = self.next
#     nodes = [];
#     nodes.append(head);
#     nodes.append(tail);
#     return "->".join(nodes);
  
# fnode = Node("Akinie","samuel");
# flink = LinkedList(fnode);
# print(f"{flink}");


#creating a complex linkedlist with some functionalities.
class LinkedList:
    """
    A class that implements a linked list data structure
    """
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0), next = None) 
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next
             





        # Make the linkedList iterable.
    def __iter__(self):
        """
        Make the linkedlist iterable
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
            nodes.append("None")
        return " -> ".join(nodes)

 



fnode = Node("Akinie","samuel");
flink = LinkedList(["Akinie","samuel"]);
print(f"{flink}");
# print(f"{flink.getNext()}");