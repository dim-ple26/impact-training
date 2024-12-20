class Node:
      def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
  def __init__(self):
   self.head=None

  def isEmpty(self):
    return self.head is None

  def append(self,data):
    new_node=Node(data)
    
    if self.isEmpty():
      self.head=new_node
      return
    current=self.head
    
    while current.next:
      current = current.next
      
    current.next=new_node
    new_node.prev=current
    
  def prepend(self,data):
    new_node=Node(data)
    
    new_node.next=self.head
    self.head.prev=new_node
    self.head=new_node
    
  def delete(self,key):
    if self.isEmpty():
      return "Empty list"
    current=self.head
    
    if current.data == key:
      if not current.next:
        self.head=None
    else:
      self.head=current.next
      self.head.prev=None
    return
  
    while current and current.data !=key:
      current=current.next

    if current.next:
      current.next.prev = current.prev
      
    if current.prev:
      current.prev.next=current.next
      
      
  def display(self):
    current=self.head
    while current:
      print(current.data, end=" <-> ")
      current=current.next
    print("\n")
      
      
dll = DoublyLinkedList()
dll.append(20)
dll.append(50)
dll.append(60)
dll.display()

dll.prepend(45)
dll.display()

dll.delete(50)
dll.display()
    
    
    
    
    