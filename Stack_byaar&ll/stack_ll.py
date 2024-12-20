class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class Stack:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head is None

  def push(self,data):
     new_node=Node(data)
     
     if self.isEmpty():
       self.head=new_node
       return
     current=self.head
     
     while current.next:
       current=current.next
     current.next=new_node
     
  def printll(self):
     current=self.head
     
     while current:
      print(current.data,end="->")
      current=current.next
     print("None")
    
  def pop(self):
    current=self.head
    while current.next:
      current=current.next
      
  
s=Stack()
s.push(10)
s.push(20)
s.printll()
    