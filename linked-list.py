class Node:
    def __init__(self, value = None , next = None):
        self.value = value       # data
        self.next = next         # reference

class Linked_List:
    def __init__(self):
        self.head = None         # head of the linked list

    def insert_last_node(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def insert_head_node(self, head_node):
        if self.head is None:
            self.head = head_node
        else:
            temp_node = self.head
            self.head = head_node
            head_node.next = temp_node
            del temp_node

    def insert_by_index(self, new_data, index):
        current_node = self.head
        if current_node is None:
            current_node = new_data
        elif index == 0:
            new_data.next = current_node
            current_node = new_data
        else:
            previous_node = None
            current_index = 0
            while current_index < index and current_node.next:
                previous_node = current_node
                current_node = current_node.next
                current_index += 1

            previous_node.next = new_data
            new_data.next = current_node
            return current_node 

    def search(self, data_search):
        current_node = self.head
        while current_node != None:
            if current_node.value == data_search:
                return print("Data is present in list")
            current_node = current_node.next
        return print("Data is not present in list")        

    def search_by_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node != None:
            if current_index == index:
                return print(current_node.value)
            current_index += 1
            current_node = current_node.next

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

    def delete_by_index(self, index):
        current_node = self.head
        if current_node:
            if index == 0:
                current_node = current_node.next
            else:
                previous_node = None
                current_index = 0
                while current_index < index and current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next
                    current_index += 1
                previous_node.next = current_node.next
        return current_node

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
link_list.insert_last_node(first_node)

second_node = Node("Supra")
link_list.insert_last_node(second_node)

third_node = Node("Adidas")
link_list.insert_last_node(third_node)

fourth_node = Node("Asics")
link_list.insert_last_node(fourth_node)

link_list.print_linked_list()
print("------After insertion of head node and by index also------")

headone_node = Node("New Balance")
link_list.insert_head_node(headone_node)

byindex = Node("Relaxo")
link_list.insert_by_index(byindex , 2)
link_list.print_linked_list()

print("-------After Deletion by index------")

link_list.delete_by_index(2)
link_list.print_linked_list()

print("----search by index----")
link_list.search_by_index(1)
