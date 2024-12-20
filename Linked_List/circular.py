class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class CircularLinkedList:
  def __init__(self):
    self.head=None
    
  def append(self,data):
    new_node=Node(data)
    
    if not self.head:
      self.head=new_node
      new_node.next=self.head
      return
    
    current=self.head
    
    while current.next!=self.head:
      current=current.next
      
    current.next=new_node
    new_node.next=self.head
    
  def prepend(self,data):
    new_node=Node(data)
    
    if not self.head:
      self.head=new_node
      new_node.next=self.head
      return
    
    current=self.head
    while current.next != self.head:
      current=current.next
    
    new_node.next=self.head
    self.head=new_node
    current.next=self.head
    
    
  def delete(self,key):
    
    current=self.head
    prev=None
    
    if current.data==key:
      if current.next==self.head:
        self.head=None
        return
      
      while current.next!=self.head:
        current=current.next
        
      current=current.next
      self.head=self.head.next
      return
    
    
    current=self.head
    while current.next != self.head and current.data !=key:
      prev=current
      current=current.next
      
    if current.data == key:
      prev.next=current.next
      
    else:
      return
    
  def print(self):
      current=self.head
      while True:
        print(current.data, end="->")
        current=current.next
        if current == self.head:
          break
      print("\n")


cll = CircularLinkedList()
cll.append(90)
cll.append(45)
cll.prepend(15)

cll.print()

cll.delete(45)
cll.print()
    
    
    
    
    
    
    