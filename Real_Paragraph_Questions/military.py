tag = input()
for i in range(len(tag)-1):
  if tag[i].lower() in ('a','e','i','o','u'):
    print("arrested")
    
  else:
    if(tag[i].isdigit() and tag[i+1].isdigit()):
      if((int(tag[i])+int(tag[i+1]))%2==0):
        print("Allowed")
        
        
