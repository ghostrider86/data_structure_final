# Linked list

A linked list is a collection of data that can be sorted in order, or a random way in memory. Each element in the linked list has a specific spot in memory, and if the data is randomized there is no way of knowing if one element is next to another. Which is why in order to organize the list, each element or in other words a **node** has a value and pointer to the next node in the list. And as shown in the picture below, the first node is known as the head. Knowing where the head is will help one taverse through the linked list.

![example of a linked list](https://www.studytonight.com/code/python/ds/images/linked-list-1.png)


## Doubly Linked List

Now the list I want you to focus on is the doubly-linked list, since most linked lists have Bi-directional linking between nodes. So instead of having only one pointer to the next node that would limit you to only go forward in the list, the doubly linked list has pointers that point to the next and previous nodes. And like the single linked list this also has a head, and in addition has a tail that points to the end of the linked list.

![Doubly Linked List](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png)

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

## Example: Playlist
In the example below, I made a simple music playlist. Which will demonstrate how to use insert head and tail into a list. the playlist shows the following:
* Inserting at the head
* Inserting at the Tail

```python
class Linked_list:
    class Node:
        def __init__(self, title, artist):
            self.title = title
            self.artist = artist
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        # Create the new node
        new_node = Linked_list.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head 
            self.head = new_node      # Update the head

    def insert_tail(self, new_node):
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.prev = self.tail # Connect new node to the previous head
            self.tail.next = new_node # Connect the previous head 
            self.tail = new_node      # Update the head 

    def display_library(self):
        curr = self.head
        while curr != None:
            print(curr.title + " By " + curr.artist)
            curr = curr.next

# music_playlist = ["Viva La vida","One more Time","At the Door","Mr.Brightside","Yellow Submarine","Black Parade","Bad Motorscooter","Crazy Horses",Yesterday]
music_lib = Linked_list()
music_lib.insert_tail(Linked_list.Node("Viva La vida", "Coldplay"))
music_lib.insert_tail(Linked_list.Node("One more Time", "Daft Punk"))
music_lib.insert_tail(Linked_list.Node("At the Door", "Strokes"))
music_lib.insert_tail(Linked_list.Node("Mr.Brightside", "The Killers"))
music_lib.insert_tail(Linked_list.Node("Yellow Submarine", "The Beatles"))
music_lib.insert_tail(Linked_list.Node("Black Parade", "MCR"))
music_lib.insert_tail(Linked_list.Node("Bad Motorscooter", "Montrose"))
music_lib.insert_tail(Linked_list.Node("Crazy Horses", "Osmunds"))
music_lib.insert_tail(Linked_list.Node("Yesterday", "The Beatles"))
music_lib.display_library()
```
Keep in mind the example shown above because you will need to use it to solve the problem ahead.
## Problem to Solve
Using the example above, write a program that will sort through and remove songs or artist from the linked list. 
| Song                 | Artist             |
| -------------------- | ------------------ |
| Viva La vida         | Coldplay           |
| One more Time        | Daft Punk          |
| At the Door          | Strokes            |
| Mr.Brightside        | The Killers        |
| Yellow Submarine     | The Beatles        |
| Black Parade         | MCR                |
| Yesterday            | The Beatles        |
| Crazy Horses         | Osmunds            |


Using the code above and these songs and artist test your program with the following scenarios:
*  Test 1: Search for song by Title and check if song is in playlist
*  Test 2: Search for all songs by artist, aka Beatles
*  Test 3: Search and remove song by title
If you need more an example or check here is a solution: [Solution](https://github.com/ghostrider86/data_structure_final/blob/main/playlist.py)


[Homepage](https://github.com/ghostrider86/data_structure_final)
