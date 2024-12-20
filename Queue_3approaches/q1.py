front = -1
rear = -1
queue_size=int(input())
queue=[]

def isEmpty():
  if front and rear == -1:
    return f"Queue is empty"

def isFull():
  if rear>=queue_size:
    return f'Queue Full'
  

def enqueue(data):
  global front,rear
  if isFull():
    return
  
  front+=1
  
  queue.append(data);
  rear+=1
  print(queue)
  
def dequeue():
  global front,rear
  if isEmpty():
    return
  else:
    front+=1
    queue.pop()
    print(queue)
  
enqueue(10)
enqueue(90)
enqueue(56)
dequeue()
  