# Queue
A Queue is a linear structure which follows a certain order that operations are performed, FIFO for short standing for first in, first out
As shown below:
![example of FIFO](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)

| Queue Operations     | Description                    | TIme Complexity      |
| -------------------- | -----------------              | -------------------- |
| Enqueue              | Adds an item to the queue      | O(1)                 |
| Dequeue              | Removes an item from the queue | O(1)                 |
| Front                | Get the front item from queue  | O(1)                 |
| Rear                 | Get the last item from queue   | O(1)                 |

## Queue Implementation
There are three different types of Queue implementation in Python: 
* List
* queue.Queue
* collections.Queue

The one we will be focusing on in this tutorial is list implementation, when it should be utilized, its effeciency, some examples, and a problem to solve using list imlplementation.

### List Implementation
In python Lists are a data structure that can be used as a queue. Which means append() and pop() can be used as replacement for enqueue() and dequeue(). Lists can be quite slow for this purpose since insering or deleting an element would require shifting all other elements by one. Which would make the dequeue operation as shown in the table above require O(n) time in lists instead of O(1).

To demonstrate how to the list data type to implement a queue, we will be going though a 7 step process
1. To make things easier we will write the queue in a class, so starts off by writing a class called Queue.
2. Next set a variable to store the data in the class, name the variable elements.

```python
class Queue:

	def __init__(self):
		self.elements = []

```
3. Inserting data into a queue aka enqueue as mentioned above we will need to use the **append()** method of the list data type to add data at the end.

```python
class Queue:

	def __init__(self):
		self.elements = []
    # step 3
    def enqueue(self, data):
		self.elements.append(data)
		return data
```
4. To remove data from a queue aka dequeue as mentioned above we will need to use the **pop()** method of the list data type to delete an element from the list of the given index, if no index is specified it will delete the last element of the list. 

```python
class Queue:

	def __init__(self):
		self.elements = []
    # step 3
    def enqueue(self, data):
		self.elements.append(data)
		return data
    # Step 4
    def dequeue(self):
		return self.elements.pop(0)
```
5. To get the method rear() to work, you just need to add negative indexing in the list data type to get the last element of the queue.
```python
class Queue:

	def __init__(self):
		self.elements = []
    # step 3
    def enqueue(self, data):
		self.elements.append(data)
		return data
    # Step 4
    def dequeue(self):
		return self.elements.pop(0)
    # Step 5
    def rear(self):
		return self.elements[-1]
```
6. To get the method front() to work, you can use the list index to get the first elemnet of the queue.
```python
class Queue:

	def __init__(self):
		self.elements = []
    # step 3
    def enqueue(self, data):
		self.elements.append(data)
		return data
    # Step 4
    def dequeue(self):
		return self.elements.pop(0)
    # Step 5
    def rear(self):
		return self.elements[-1]
    # Step 6
    def front(self):
		return self.elements[0]
```
7. To find out if the queue is empty, that can be done by checking the length of the list using **len()** and checking if the list size equals 0.
```python
class Queue:

	def __init__(self):
		self.elements = []
    # step 3
    def enqueue(self, data):
		self.elements.append(data)
		return data
    # Step 4
    def dequeue(self):
		return self.elements.pop(0)
    # Step 5
    def rear(self):
		return self.elements[-1]
    # Step 6
    def front(self):
		return self.elements[0]
    # Step 7
    def is_empty(self):
		return len(self.elements) == 0
```


## Example of Queue List Implementation
In the example below is an example of list implementation. This program is a customer service call list. Which add members to a call list and add or removes them from the list when the employee finishes talking to them.
* randomly puts call on the call queue
* displays which employee is working with each member
* removes satisfied members from call list
* checks if member is in call, returning true or false 

```python
import random
call_queue = []
employee_list = []

# This is going to randomly put calls onto the call queue
def phone_system_update():
    if random.randint(0,3) == 1:
        phone_queue_call(random.randint(1,50)) #A call from 1 in 50 random members

def phone_queue_call(member_id):
    call_queue.append(member_id)
    print(f"The call queue is now {call_queue}")

def phone_deqeue_call(employee_id):
    if len(call_queue) > 0:
        member_id = call_queue.pop(0)
        print(f"Employee id: {employee_id} is now working on a call with member:{member_id}")
        employee_list[employee_id] = True
    else:
        print("No calls in the queue")
def customer_service():
    #check each employee
    for i in range(0,len(employee_list)-1):
        if not employee_list[i]: # if they are not on the line
            phone_deqeue_call(i) # pick up a waiting call
        else:      
            if random.randint(0,3) == 1:    #are they done with the call
                employee_list[i] = False    #hangup

# init employee list
for i in range(0,3):
    employee_list.append(False)
while True:
    phone_system_update()
    customer_service()
```

## Problem to solve
To practice using queue in python write a program that sorts a shopping list. 
make sure that three variables can be added to the list
* food, what kind of food it is
* type, what food group does it belong to
* Favorite, why you like this type of food.

1. Have a add_food function that enqueus food into the queue
2. add a limit to how much food can be added for example 6, if the queue is full it should display an error message
3. If queue is empty display an error message
4. have a favorite list funtion that dequeues the food from the queue and displays the details

Once you have written these functions try to have it pass these tests:
1. Test 1: Can I add one food and finish my food list?
2. Test 2: Does the max queue size get enforced?
3. Test 3: Can I add two foods and have the food list in the correct order?
4. Test 4: Can I food to the list if there is no food?

If you are stuck or need a reference a possible solution is provided:
[solution link](https://github.com/ghostrider86/data_structure_final/blob/main/food_list.py)


[Homepage](https://github.com/ghostrider86/data_structure_final)
