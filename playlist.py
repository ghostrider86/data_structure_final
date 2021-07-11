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
            self.tail.next = new_node # Connect the previous head to the new node
            self.tail = new_node      # Update the head to point to the new node

    def search_by_title(self, title):
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.title == title:
                return curr
            curr = curr.next # Go to the next node to search for 'value'
        return None

    def search_by_artist(self, artist):
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        artist_list = Linked_list()
        curr = self.head
        while curr is not None:
            if curr.artist == artist:
                artist_list.insert_tail(curr)
            curr = curr.next # Go to the next node to search for 'value'
        return artist_list

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None  
            self.head = self.head.next  

    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None  
            self.tail = self.tail.prev  


    def remove_by_title(self, title):
        curr = self.search_by_title(title)
        if curr is not None:
            if curr == self.tail:
                self.remove_tail()
            elif curr == self.head:
                self.remove_head()
            else:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
            return 


    def display_library(self):
        curr = self.head
        if curr == None:
            print("No songs in Playlist")
        while curr != None:
            self.display_song(curr)
            curr = curr.next

    def display_song(self,curr):
        if curr != None:
            print(curr.title + " By " + curr.artist)
        else:
            print("song not in playlist")



    
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
print("\n-------- Sample 1  ----------")
#Test 1
# Search for song by Title and check if song is in playlist
node = music_lib.search_by_title("One more Time")
music_lib.display_song(node)
node = music_lib.search_by_title("No more tears")
music_lib.display_song(node)
print("\n-------- Sample 2  ----------")
#Test 2
# Search for all songs by artist, aka Beatles
new_list = music_lib.search_by_artist("The Beatles")
new_list.display_library()

new_list = music_lib.search_by_artist("ozzy")
new_list.display_library()

print("\n-------- Sample 3  ----------")
#Test 3
# Search and remove song by title
music_lib.remove_by_title("Black Parade")
music_lib.display_library()
