
top=-1
stack=[]
def push(data):
  global top
  
  top+=1    
  stack.append(data)
  print(f"Push:{data}")
  print(stack)
  
  
def pop():
  global top
  
  if top >= 0: #check not empty
     data=stack[top]
     stack.pop()
     top-=1
     print(f"pop:{data}")
     print(stack)
  else:
    print("Stack is empty ....Can't pop")

  
def overflow():
  global top
  if top>len(stack):
    print("OverFlow")
  
def underflow():
  global top
  if top==-1:
    print("underflow")
    
  
underflow()
push(10)
push(20)
push(30)
pop()


    
    