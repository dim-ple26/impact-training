class Node:
   def __init__(self,data):
     self.data=data
     self.next=None
     
class SingleLinkedList:
  def __init__(self):
    self.head = None
    
  def isEmpty(self):
    return self.head is None

  def append(self,data):
    new_node = Node(data)
  
    if self.isEmpty():
      self.head=new_node
      return
    current = self.head
    
    while current.next:
      current = current.next
      
    current.next=new_node
  
  def prepend(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
    
  def insert(self,prev_data,new_data):
    current=self.head
    while current and current.data !=prev_data:
      current=current.next
    if not current:
      print(f"Node with the data {prev_data} not found")
      return
    new_node=Node(data)
    new_node.next=current.next
    current.next=new_node
    
  def delete(self,key):
    current=self.head
    
    if current and curent.data == key:
      self.head = current.next
      current=None
      return
    prev=None
    while current==current.data!=key:
      prev=current
      current=current.next
    if not current:
      print(f"Node with the data {key} is not found")
      return
    
    prev.next=current.next
    current=None
    def printll(self):
      current=self.head
      
      while current:
        print(current.data,end="->")
        current=current.next
      print("None")
      
      
sl=SingleLinkedList()
sl.append(10)
sl.append(20)
sl.append(30)
print("Initial list")
sl.printll()
sl.prepend(50)
sl.insert(2,15)

print("after inserting 15")
sl.printll()
print("deletion")
sl.delete(20)


      
      
    
  
