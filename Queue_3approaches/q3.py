class Queue:
  def __init__(self,size):
    self.size=size
    self.queue=[]
    
  def enqueue(self,item):
    if len(self.queue)<self.size:
      self.queue.append(item)
      print(f'{item} is inserted')
    else:
      print(f'Queue is Full')
      
  def dequeue(self):
    if self.queue:
      item=self.queue.pop(0)
      print(f'{item} deleted from queue')
      
    else:
      print('Queue is Empty')
  
  def display(self):
    print("The elements are in the queue are:")
    print(*self.queue)
    

size=5
q=Queue(size)

q.enqueue(10)
q.enqueue(90)
q.display()

q.dequeue()
q.display()