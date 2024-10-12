import queue
q = queue.Queue()
q.put('a')
q.put('b')
q.put('c')

while not q.empty():
    print(q.get())

print(q.full())

