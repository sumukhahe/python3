m=int(input('Enter m:'))
n=int(input('Enter n:'))
def prime(m,n):
    for a in range(m,n+1):
        if a>1:
            for b in range(2,a):
                if(a%b)==0:
                    break
            else:
                print(a)
                    
if(m>0 and n>0 and m<n):
    prime(m,n)
else:
    print('Enter suitable Integers')
