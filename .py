import random
call_queue = []
employee_list = []
# employee_list = []

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