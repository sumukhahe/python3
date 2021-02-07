
def collatz(number):
    while number!=1:
    
        if(number%2==0): # Even number
            number=number//2
            print(number)
                
        elif(number%2==1): # odd Number 
            number=3*number+1
            print(number)
                
        elif(number==1):
            print(number)

try:
    print('enter a number')
    number=int(input())
    collatz(number)
    
except:
        print('Enter an integer')
