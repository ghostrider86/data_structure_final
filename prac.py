import queue
q = queue.Queue()
q.put('how')
q.put('are')
q.put('you')
q.get(0)
print(q)