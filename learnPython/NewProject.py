class Contact:
    def __init__(self):
        # This contains list of contacts already in a dictornary
     self.contacts = {
        "samuel":"0209344294",
        "simon":"0595993075",
         "kwame": "0542642482"
        };

# Adding a contact to ahone directory.
    def add(self,name,phone):  
      #item() makes the dictornary iterable so we can iterate through the dictionary  
       for key,value in self.contacts.items():
         #if the name the user enters is equal to any of them in the dictionary, then we return "Name already exists"
            if key == name:  
                return "Name already exists 🥲";     
       # if the name the user entered was not found, we then add it to the dictionary 
       self.contacts[name] = phone;
       return "Name has been added to Contact 😊";

# add the number to it.
    def delete(self,name):
        for key,value in self.contacts.items():
            # if name is found in the dictionary, we use the "del in-built method" to delete an item in a dictionary. 
            if key == name:
             del self.contacts[name];
             return name + " has been deleted";
            #  if name doesn't exist in the dictionary, we say Name does not exists
        return "Name does not exist 🥲";    
     

    # Search for a name 
    def search(self,name):
        for key,value in self.contacts.items():
            # if name is found in the dictionary, we return the name plus the phone number which is the same as the value
            if key == name:
                return (key + " -> " + value);
        return name + " was not found 🥲";

    def Edit(self,name,number):
        for key,value in self.contacts.items():
            # if name is found in the dictionary, we then update it.
            if key == name:
                self.contacts[name] = number; 
                return "Number was updated successfully";
                # if name wasn't found, we tell the user name was not found.
        return name + " was not found, why don't you create a new one? 😊";          
    
    def All(self):
        # if user wants to see all the contacts, we return all the contacts
        return self.contacts
# creating an instance of a class
contact = Contact();    

# we are returning the values so we will need to do print() in order to see the result

# print(contact.add("samuels","020525256555"));
# print(contact.delete("kwame"));
# print(contact.search("kwame"));
# print(contact.All());





















# This gives you Samuel already exists
# contact.add("samuel","45");
# print(contact.add('samuel',30));

# # Note we don't say contact.self.name();
# print(contact.name);

# print(contact.delete("menzgold"));


# print(contact.search("samuel"));




# ideas

# print(key, '->', a_dict[key])