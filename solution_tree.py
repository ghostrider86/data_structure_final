class Binary_Search_Tree:

    class Song:
        def __init__(self, index, artist, song):
            self.index = index
            self.artist = artist
            self.song = song

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Binary_Search_Tree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data.song == node.data.song and data.artist == node.data.artist:
            return
        elif data.song < node.data.song:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = Binary_Search_Tree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = Binary_Search_Tree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __iter__(self):
        yield from self.traverse_forward(self.root)  # Start at the root

    def traverse_forward(self, node):
        if node is not None:
            yield from self.traverse_forward(node.left)
            yield node.data
            yield from self.traverse_forward(node.right)

    def display_library(self):
        for x in self.traverse_forward(self.root):
            print("Song: " + x.song + " Artist: " + x.artist)


    def search_song(self,song):
        for x in self.traverse_forward(self.root):
            if (x.song == song):
                return True
        return False

    def search_artist(self,artist):
        for x in self.traverse_forward(self.root):
            if (x.artist == artist):
                print("Song: " + x.song + " Artist: " + x.artist)



print("\n===========  Example 1 TESTS ===========")
music_tree = Binary_Search_Tree()
#self.root = BST.Node(data)
music_tree.insert(Binary_Search_Tree.Song(1,"Coldplay","Viva La vida"))
music_tree.insert(Binary_Search_Tree.Song(2,"Daft Punk","One more Time"))
music_tree.insert(Binary_Search_Tree.Song(3,"Strokes","At the Door"))
music_tree.insert(Binary_Search_Tree.Song(4,"The Killers","Mr.Brightside"))
music_tree.insert(Binary_Search_Tree.Song(5,"The Beatles","Yellow Submarine"))
music_tree.insert(Binary_Search_Tree.Song(6,"MCR","Black Parade"))
music_tree.insert(Binary_Search_Tree.Song(7,"Montrose","Bad Motorscooter"))
music_tree.insert(Binary_Search_Tree.Song(8,"Osmunds","Crazy Horses"))
music_tree.insert(Binary_Search_Tree.Song(9,"The Beatles","Yesterday"))

music_tree.display_library()

print("\n-------- Sample 1  ----------")
#Test 1
# Search for song by Title and check if song is in playlist
if music_tree.search_song("One more Time"):
    print("Song in playlist")
if music_tree.search_song("No more tears"):
    print("Song in playlist")

print("\n-------- Sample 2  ----------")
#Test 2
# Search for all songs by artist, aka Beatles
music_tree.search_artist("The Beatles")


