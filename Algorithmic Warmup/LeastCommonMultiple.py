#Python 3
def CalGCD(a,b): 
    if a == 0: 
        return b 
    return  (int (CalGCD(b % a, a))) 

def CalLCM(a,b): 
    return (int(a*b) // CalGCD(a,b) )
user_input = input()
a, b = map(int, user_input.split())
print (int(CalLCM(a, b)))
