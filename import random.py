import random
a=1  
B=100  
hads=random.randint(a,B)   
print(hads)  
javab="This is the javab"   
# *************  
 
while javab  != "d":  
    javab=input()   
   
    if(javab == "k"):  
        B=(hads-1) 
        hads=random.randint(a,B)  
        print(hads) 
    elif(javab == "b"):  
        a=(hads+1)  
        hads=random.randint(a,B)  
        print(hads) 
    
       
                