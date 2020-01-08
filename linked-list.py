class Node:

    def __init__(self, value):
        self.value = value       # data
        self.next = None         # reference

class Linked_List:

    def __init__(self):
        self.head = None         # head of the linked list


    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node


    def search(self, data_search):

        current_node = self.head
        while current_node != None:
            if current_node.value == data_search:
                return print("Data is present in list")
                
            current_node = current_node.next
        return print("Data is not present in list")        


    def delete(self, data_delete):

        current_node = self.head
        if current_node != None: 
            if current_node.value == data_delete: 
                self.head = current_node.next
                current_node = None
                return
  
        while current_node != None: 
            if current_node.value == data_delete: 
                break 
            previous = current_node 
            current_node = current_node.next 
  
        if(current_node == None): 
            print("Data not present")
            return 
  
        previous.next = current_node.next 
        current_node = None


    def print_linked_list(self):

        if self.head is None:
            print("Empty list")

        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.value)
            current_node = current_node.next




link_list = Linked_List()

first_node = Node("Nike")
link_list.insert(first_node)

second_node = Node("Supra")
link_list.insert(second_node)

third_node = Node("Adidas")
link_list.insert(third_node)

fourth_node = Node("Asics")
link_list.insert(fourth_node)
link_list.print_linked_list()

link_list.delete("Adidas")
print("After deletion")
link_list.print_linked_list()