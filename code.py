def Calculo_Brute_Force(x):
    
    for a in range(1,x+1):
            if ((a*a)>x) :
                print (a,a)
                return(a,a)
    
    print(-1)
    return(-1)

Calculo_Brute_Force(int(input()))