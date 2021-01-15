#python 3
def findMin(V): 
        
    deno = [1, 5, 10] 
    n = len(deno) 
     
    ans = [] 
  
    i = n - 1
    while(i >= 0): 
          
        while (V >= deno[i]): 
            V -= deno[i] 
            ans.append(deno[i]) 
  
        i -= 1
     
    print( len(ans)) 
   
if __name__ == '__main__': 
    n =int(input())
    findMin(n) 
   
