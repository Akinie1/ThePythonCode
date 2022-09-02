class Node:
    """
    A class that implements a node of a linked list
    """
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, item):
        self.data = item

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return self.data



# fnode = Node("Samuel","Simon") 
# fnode.set_next("NextValue here");
# print(f"{fnode.next}")



class LinkedList:
    def __init__(self,head):
       self.head = head.data;
       self.pointer = head.next
         
    def __repr__(self):
        node = self.head
        nodes = ["head"];
        while node is not None:
            nodes.append(self.head)
            nodes.append(self.pointer)
            nodes.append("tail")              
            return "---------->".join(nodes);
    


fnode = Node("Alex","Akinie");
# # LinkedList.head = fnode
# print(f"{fnode}");
# # print(f"{LinkedList.head}")
# link = LinkedList();
print(f"{LinkedList(fnode)}")


# link = LinkedList(fnode);


# print(f"{link}")










