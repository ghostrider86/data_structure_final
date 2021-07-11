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


