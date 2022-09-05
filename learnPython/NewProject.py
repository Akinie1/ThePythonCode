class Contacts:
    def __init__(self):
        # self.map is the hash table
        #self.size is the size the hash table.
        self.size = 6   
        self.map = [None] * self.size   
     
    #  This function returns a unique identifier which then links to the hash table's index
    #The ord() function returns the number representing the unicode code of a specified character.

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
         hash += ord(char)   #ord() converts the letters of each string into an Anscii
        return hash % self.size

  

    def add(self, key, value):
        #key_value variable contains your name and teh value  eg ['samuel','0209344294']  
        key_hash = self._get_hash(key)  # goes to get the unique index 
        key_value = [key, value]  
       
    #  using that unique key value to insert as an index to the self.map which is the hashed table.
        if self.map[key_hash] is None: 
            # we are just storing the values inside the self.map array.
            self.map[key_hash] = list([key_value])  #the self.map contains the field in that index row of the hashed table which was generated from the hashing algorithm.
            return key + " has been added to the table👤"
        else:
          #so if the self.map[key_hash] which is the field in that index row in the hash table has a value inside, we iterate through that field and we check if the key the user entered is the same as the one in the hash table.
            for pair in self.map[key_hash]:
            #   if by chance the key the user entered is the same as the the key in the field in the hash table, we just add the value.
                if pair[0] == key:  #so if keys are the same, then we tell teh user "Contact already exists"
                 return "Contact already exists.🥲"

 

# Gets result based on a specific key.
    def search(self, key):

        #remember to solve the case sensitive 
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:  #so we are iterating through field in teh hash table.
                if pair[0] == key:  
                    if(pair[0] == 'wife'):
                        return pair[0] + "❤️ " + "->" + pair[1]
                    if(pair[0] == 'Home'):
                        return pair[0] + "👨‍👩‍👦‍👦 " + "->" + pair[1]   
                    if(pair[0] == 'Police'):
                        return pair[0] + "👮 " + "->" + pair[1]  
                    return pair[0] + "->"+ pair[1]  #we are returning the value over here if the values typed in are the same.
    #if through the iteration, the keys weren't the same then we say No contact exists.
        return "No contact exists🥲"  

    # delete a result based on a certain key.
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return "No contact exist to be deleted"
      #we use the range because the because we are iterating through for the index
        for i in range(0, len(self.map[key_hash])):  #This is like for loop.
            if self.map[key_hash][i][0] ==  key:  #we are iterating through the keys value pairs in the linked list. We iterate because the linked list might be more than one since collisions can occur, we introduced the concept of a linkedlist.
                self.map[key_hash].pop(i)  
                return key + " has been deleted successfully"



    def print(self):
        print("")
        print("::::::PHONEBOOK DIRECTORY::::::")
        print("")
       
#since the self.map is the whole phonebook directory. so we are iterating through the phone directory and if the the item is not None, we display the array in a string format.
        for item in self.map:
            if item is not None:
     
             return (str(item))
      
      

# Edit function.
# How to edit the phonebook directory, so we pass in the key we want to edit and then pass in the name and the value 
    def Edit(self,key,name,value):
        key_hash = self._get_hash(key)
        for i in range(0,len(self.map[key_hash])):
         if(self.map[key_hash][i][i] == key):    
            self.map[key_hash][i][i] = name
            self.map[key_hash][i][i+1]= value
            return "Contact was edited successfully"

         return "No such contact was found"

# Instantiating the class.
C = Contacts()
# Adding the values to the hash table.
print(C.add("wife","0209344294"))  
print(C.add("Home","0209344294"))   
print(C.add("Police","0209344294"))

# print(C.get("wife"))
# print(C.delete(""))
# print(C.Edit("wife","girlfriend","0000000"))
# print(C.print())

# print(C.Edit("Home","family","0000"))































































