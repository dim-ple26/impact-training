def handle_exceptions():
  try:
       print("Dividing By Zero:")
       result = 10 / 0 
       
  except ZeroDivisionError as e:
       print(f"Caught a ZeroDivision Error : {e}")
       
  try:
      print("\nConverting invalid string to integer:")
      result = int("abc")
      
  except ValueError as e:
      print(f"Caught a ValueError: {e}")
      
      
  try:
      print("\nAccesing out-of-range index in a list:")
      my_list = [1,2,3]
      result = my_list[5]
      
  except IndexError as e:
      print(f"Caught an IndexError: {e}")
      
      
  try:
      print("\nAccesing non-existent key in a dictionary:")
      my_dict={"a":1,"b":2}
      result=my_dict["c"]
      
  except KeyError as e:
      print(f"Caught a KeyError:{e}")
      
      
  try:
      print("\nAdding incompatible types: ")
      result=10+"20"
      
  except TypeError as e:
    print(f"Caught a TypeError:{e}")
    
  
