# Linked list

Linked lists are sequences of data elements, connected via links. The data elements contain connection to another through pointers. Since the Python library does not have linked list in its standard library, we implement linked list through nodes. A node is a combination of the value and the pointers representing one item in the linked list.

 

## How to create a linked list

As mentioned before of the importance on Nodes we will using them to make a linked list. By creating a Node object and creating another class to use the Node object,  and by passing the appropriate value through the node object which will point to the next data elements.

```python
class Node:
    def __init__(self,data_value = None):
    self.data_value = data_value
    self.next_value = None
class Link_List:
    def __init__(self):
        self.head_value = None
link_list_1 = Link_List()
link_list_1. head_value = Node("Sun")
num_2 = Node("Mon")
num_3 = Node("Tue")
# The code below will Link the first node to second one
link_list_1.head_value.next_value = num_2
# The code below will Link the 2nd node to 3rd one
num_2.next_value = num_3
```
## How to transverse through a linked list
when you transverse through a linked list you can only go on the forward direction from the first data element. Then print the value of the next data element by assigning the pointer of the next node to the current data element.

```python
class Node:
    def __init__(self,data_value = None):
    self.data_value = data_value
    self.next_value = None

class Link_List:
    def __init__(self):
        self.head_value = None

    def printed_list(self):
        while printed_value is not None:
            print(printed_value.data_value)
            printed_value = printed_value.next_value
link_list_1 = Link_List()
link_list_1. head_value = Node("Sun")
num_2 = Node("Mon")
num_3 = Node("Tue")
# The code below will Link the first node to second one
link_list_1.head_value.next_value = num_2
# The code below will Link the 2nd node to 3rd one
num_2.next_value = num_3
list.printed_list()
```

The expected output should be:
* Sun
* Mon
* Tue

## How to use insertion in a linked list
To insert an element into a linked list you need to reassign the pointers from existing nodes with a newly inserted node. There are three ways a new data element can be inserted which is at the head, middle or tail of the linked list. 

### Inserting at the head
The new node is added before the head on the linked list. With the added node becoming the new head of the linked list. And this typically a 4 step process.
1. Allocate the Node
2. Put in the data
3. Makes the new Node as head
4. Moves the head to pointer of the new Node

```python
    def push(self, new_data):
        new_node = Node(new_data) #step 1&2
        new_node.next = self.head #step 3
        self.head = new_node #step 4
```

![example of FIFO](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_at_start.png)

### Inserting in the middle
To add a node in the middle, once you have the pointer to a node, you can add the new node after node that was pointed too.And this typically a 5 step process.

1. check if the node pointed too exists
2. Create a new node
3. Put in the data
4. Moves the head to pointer of the new Node
5. Make the new Node as the prev_node

```python
    def insert_middle(self, prev_node, new_data)
        if prev_node is None: #step 1
            print("does not exist")
            return
        new_node = Node(new_data) #step 2&3
        new_node.next = prev_node.next #step 4
        prev_node.next = new_node #step 5
```

![example of FIFO](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_middle.png)

### Inserting at the tail
To add a node to the end, it needs to be added after the last node of the linked list. You may also have to transverse the list till the end and then change the next to last node to a new one And this typically a 6 step process.

1. Create a new node
2. Put in the data
3. Set next as None
4. If the Linked List is empty, then the new node becomes the head
5. Else traverse till the last node
6. Change the next of last node

```python
    def append(self, new_data):
        #step 1 - 3
        new_node = Node(new_data)
        #step 4
        if self.head is None:
            self.head = new_node
            return
        #step 5
        last = self.head
        while (last.next):
            last = last.next
        #step 6
        last.next =  new_node
```

![example of FIFO](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_last.png)

## Removing an item
As well as inserting you can remove an exsisting node, using the key of that node. Which can be done by locating the previous node that is to be deleted then the pointer of the node of the next node is deleted. 

```python
class Node:
    def __init__(self,data_value = None):
    self.data_value = data_value
    self.next_value = None

class Link_List:
    def __init__(self):
        self.head_value = None

    def the_begining(self, data_in)
        new_node = Node(data_in)
        new_node.next = self.head
        self.head = new_node

    #def to remove a node
    def remove_node(self, remove_key)
        head_value = self.head
        if head_value is not None:
            if(head_value.data == remove_key):
                self.head = head_value.next
                head_value = None
                return
        while head_value is not None:
            if head_value.data == remove_key:
                break
            previous = head_value
            head_value = head_value.next
        if head_value == None:
            return
        previous.next = head_value.next
            head_value = None
    
    def print_list(self):
        print_value = self.head
        while print_value:
            print(print_value.data)
            print_value = print_value.next

link_list_1 = Link_List()
link_list_1.the_begining("Sun")
link_list_1.the_begining("Mon")
link_list_1.the_begining("Tue")
link_list_1.the_begining("Wed")
link_list_1.remove_node("Mon")
link_list_1.print_list()
```
The expected output should be:
* Wed
* Tue
* Sun