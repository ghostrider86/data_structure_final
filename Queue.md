# Queue
A Queue is a linear structure which follows a certain order that operations are performed, FIFO for short standing for first in, first out
As shown below:
![example of FIFO](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)
When it comes to queues in python there are four main operations

## Queue Implementation
There are three different types of Queue implementation in Python: 
* List
* queue.Queue
* collections.Queue

**I will describe each one briefly but the one I will be USING IN MY EXAMPLE CODE will be list implementation.**

### List Implementation
In python Lists are a data structure that can be used as a queue. WHich means append() and pop() can be used as replacement for enqueue() and dequeue(). Repeating the example above but with list implementation:

```python
q = []
q.append('how')
q.append('are')
q.append('you')
q.pop(0)
```
Just like the answer above it pops or removes the first in the list and we are left with "are you" in the queue.

### queue.Queue Implementation
Queue is a built in module in python that implements a queue, which initilizes a variable to a max size. Operations are as follows:

* full(),returns True if there are maxsize items in the queue.
* get(), This removes and return an item from the queue.
* put(item),Puts an item into the queue.
* maxsize, sets the number of items allowed in the queue.
* empty(), checks if the queue is empty and returns True, False otherwise.

#### Operations in Python 

1. Enqueue, which adds an item to the queue.
2. Dequeue, Removes an item from the queue. The items are popped in the same order in which they were pushed.
3. Front, Gets the front item from queue.
4. Rear, Gets the last item from queue. 

For example lets say we have the following:
```python
import queue
q = Queue()
q.enqueue('how')
q.enqueue('are')
q.enqueue('you')
q.dequeue()
```
If there was no dequeue at the end it would simply say "how are you" but since there is we apply FIFO which would remove the first item in the list and we are left with "are you"

### collections.deque Implementation
As shared previously that queue in Python can be implemented using deque, and deque is preferred over lists when quicker pop and append operations are needed. So instead of enqueue and deque, append() and popleft() functions are used.

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
