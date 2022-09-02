class Node:
    """
    A class that implements a node of a linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, item):
        self.data = item
        return self.data;

    def set_next(self, next):
        self.next = next

    def __repr__(self):
       return self.data


# Linkedlist
class LinkedList:
    """
    A class that implements a linked list data structure
    """
    #if you use nodes.pop(), it affects the original content.
    def __init__(self, nodes=None):
        self.head = None
        self.nodes = nodes; 
        if nodes is not None: #This code will run because nodes is not none.
            # NODES.POP(0) - THIS GIVES US THE HEAD. BECAUSE NODES.POP(0) RETURNS THE FIRST VALUE
            node = Node(data=nodes.pop(0))   #WE GET THE HEAD.
            #The code means we are sending the head in the node class and receiving the that back in the __repr__ 
            self.head = node  #THIS GAVE US THE HEAD. and if this gives us the head, we use that  value in the insert_first() function to insert a new node at the head. 

            for item in nodes: #nodes refers to the array or list
                node.next = Node(data=item) #we get tail here, because since the nodes.pop(0) affects the orignial function and we have removed it, printing out nodes will give us only the tail.
                #won't the node.next give us the tail since the last iteration will replace the first iteration value node.next 
                print(f"{item}");   #we get tail.
                node = node.next
  
    
    def func(self):
        # THIS FUNCTION SHOULD GIVE YOU THE TAIL BECAUASE YOU HAVE REMOVED THE HEAD AND THAT FUNCTION THAT IS USED TO REMOVE THE VALUES AFFECTS THE ORIGNAL VALUE. 
        return self.nodes;

    def anotherfunc(self):
        return self.head;   

#instantiating an object 
fnode = Node("Samuel","Menzgold");
# print(f"{fnode}");

linkedLists =  LinkedList(nodes = ["head","tail"]);

print(f"{linkedLists.func()}");

# print(f"{linkedLists.anotherfunc()}");

# values = ["samuel","menzgold","kwame"];
# values1 = values.pop(0);
# print(f"{values1}");