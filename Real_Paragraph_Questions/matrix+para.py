#N=int(input()) #men
#M=int(input()) #women


matrix = [[1,0,0],[0,1,1],[1,1,1]]

        
def count_collisions(matrix):
    rows = len(matrix) #men
    cols = len(matrix[0]) #women
    
    collisions = 0
    

    for j in range(cols):
      
        count = sum(matrix[i][j] for i in range(rows))
        #count of men liking women
        
    
        if count >= 2:
            collisions += (count * (count - 1)) // 2
    
    return collisions
    
result=count_collisions(matrix)
print(f"{result}")


  
    
      





    