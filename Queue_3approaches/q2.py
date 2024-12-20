class Queue:
  def _init_(self,size):
    self.sizes=size
    self.queue=[None]*size
    self.front=self.rear=-1
    
  def enqueue(self,item):
    if (self.rear+1) % self.size==self.front:
      print(f'Queue is full')
    else:
      if self.front==-1:
        self.front=0 
      self.rear=(self.rear+1)%self.size 
      self.queue[self.rear]=item
      print(f'{item} is inserted')
      
  def dequeue(self):
    if self.front==-1: 
     print(f'Queue is Empty')
     return
    else:
      item=self.queue[self.front]
      if self.front==self.rear:
        self.front=self.rear=-1
      else:
        self.front=(self.front+1) %self.size
      print(f'{item}is deleted from Queue')
      return
      
  def display(self):
    if self.front==-1:
      print("Queue is Empty")
    else:
      print(f"Queue elements are: ")
      
      i=self.front
      
      while True:
        print(self.queue[i],end=" ")
        
        if i==self.rear:
          break
        
        i=(i+1)%self.size
      print()  
        
    
size=5
q=Queue(size)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)