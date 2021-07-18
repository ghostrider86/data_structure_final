#Trees
When you have a linked list that has nodes its known as a tree. The nodes are connected by pointers, and what’s nice about a tree is that you can connect to multiple different nodes. And in this tutorial, we will discuss what makes up a binary tree, and a binary search tree(BST for short).

## Binary tree

What makes a tree into a binary tree is when it links to at maximum two other nodes. A binary tree node has the following components:

* Data
* pointer to right child
* pointer to left child

![Picture of binary tree](https://miro.medium.com/max/975/1*PWJiwTxRdQy8A_Y0hAv5Eg.png)


As shown in the picture above these are the key terminologies related to a binary tree
 

**Node** - The most elementary unit of a binary tree.
**Root** - The root of a binary is the topmost element. There is only one root in a binary tree.
**Leaf** - The leaves of a binary tree are the nodes which have no children.
**Level** - The level is the generation of the respective node. The root has level 0, the children of the root node is at level 1, the grandchildren of the root node is at level 2 and so on.
**Parent** - The parent of a node is the node that is one level upward of the node.
**Child** - The children of a node are the nodes that are one level downward of the node.

### Implementing a binary tree

First you need to initialize a node class, which can be done by defining the node class.

```python
# The Node class defines the structure of a Node
class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None #left child
        self.right = None #right child
        self.data = data #Node data
```

When you have the Node class defined you can start initializing the binary tree:

```python
class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None #left child
        self.right = None #right child
        self.data = data #Node data
    def print_tree(self):
        print(self.data)
root = Node(12)
root.left = Node(24)
root.right = Node(86)
root.print_tree()
# the root gets initialized to 10 and then we add 24 to the left and 86 to the right with the tree structure # looking something like this
# Binary Tree
#                       12
#                      /  \       
#                    24    86
```
## Binary search tree

This follows the same rule as a binary tree but contains more nodes, and when data is placed into the BST it compares the data with the value of the parent. Then depending on if the data is greater or less then the parent node it will go either left or right.

We always start at the root which in this example is 8, now lets say for example we wanted to insert 4. 
We would compare 4 with 8, and since 4 is less then 8 it would go left.
Next compare 4 with 3, and since 4 is greater it will go to the right this time. 
Lastly 4 is compared with 6, and since 4 is less then 6 it goes to the left, 
where 4 would be inserted into the empty node left of 6.
![Picture of BST](https://media.geeksforgeeks.org/wp-content/uploads/BSTSearch.png)

### Inserting into a Binary Search Tree
When inserting data into a tree we can use the same node class in the example above and add an insert class to it. The insert
class compares the value of the node to the parent node and depending if it more or less it goes right or left. Then the tree is printed

 ```python
class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Compare the new value with the parent node
    def insert(self, data):
      if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
      else:
         self.data = data
# Print the tree
    def print_tree(self):
      if self.left:
         self.left.print_tree()
      print( self.data),
      if self.right:
         self.right.print_tree()
# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()
 ```

The expected Output of the code above, should output: 3,6,12,14

### traversing through a Binary Search Tree
When you traverse through a BST you want to display all the data contained in the tree. There are a few way to transvere through a BST. The Two we will go over is ordered and reversed Traversal. An ordered traversal goes from the smallest node to largest, with the opposite being from largest to smallest which would be a reverse Traverse. 

#### Recursion
Since binary trees have subtrees this allows us to use recursive functions. Recursion(Which means the function calls itself). is the process of breaking up a larger problem into smaller easier to solve problems. The condition where the soultion is found in known as the base case. Which allows the function to continually call itself, passing data that continuely gets smaller till the base case is reached. 
```python
    def __iter__(self):
        yield from self.ordered(self.root)  
    # To do an ordered traversal you need to start with the root, which become the base case thats called whenever there is a loop

    def ordered(self, node):
        if node is not None:
            #if the node is not empty it will traverse from smallest to greatest and return a value to the for loop, this also helps avoid infinite recursion since if its empty its already solved
            yield from self.ordered(node.left)
            yield node.data
            yield from self.ordered(node.right)
        
```
A reversed Traverse is extremely similar except that instead of smallest to greatest, its greatest to smallest

```python
    def __iter__(self):
        yield from self.reverse(self.root)
    # To do an ordered traversal you need to start with the root, which become the base case thats called whenever there is a loop

    def reverse(self, node):
        if node is not None:
            #if the node is not empty it will traverse from greatest to smallest so right to left
            yield from self.reverse(node.right)
            yield node.data
            yield from self.reverse(node.left)
```

## Example: Playlist
In the example below, I made a simple music playlist. Which will demonstrate:
* Inserting into the tree
* printing the playlist in order

```python
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
            self._insert(data, self.root)  #root

    def _insert(self, data, node):
        if data.song == node.data.song and data.artist == node.data.artist:
            return
        elif data.song < node.data.song:
            # The data goes to the left side.
            if node.left is None:
                # We found an empty spot
                node.left = Binary_Search_Tree.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                # found an empty spot
                node.right = Binary_Search_Tree.Node(data)
            else:
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
            print("Song: " + x.song + "Artist: " + x.artist)

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
music_tree.insert(Binary_Search_Tree.Song(9,"Yesterday","Viva La vida"))
music_tree.display_library()

```

Keep in mind the example shown above because you will need to use it to solve the problem ahead.
## Problem to Solve
Using the example above, write a program that will sort through songs, check if there in the playlist, and search by artist.
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
If you need more an example or check here is a solution: [Solution](https://github.com/ghostrider86/data_structure_final/blob/main/playlist.py)


[Homepage](https://github.com/ghostrider86/data_structure_final)
