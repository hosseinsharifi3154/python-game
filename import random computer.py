import random
a=1  
B=100 
hads=random.randint(a,B)     
javab="This is the javab"
counter=0
counter=int(counter)
# *************  
print("Enter your name: ")
name=input()
print("Hi %s, lets go and guess my answer: " % (name)) 

# ************* 
while javab  != hads: 

    javab=input()
    javab=int(javab)   
    counter += 1
    if(counter>9):
        print("Oh , %s , you lose... " % (name))
        break
    if(javab > hads):    
        print("javab kochik tare!!!!!") 
    elif(javab < hads):   
        print("javab bozorg tare!!!!!")
    elif (javab == hads):
        print("wooooow, %s you win" % (name))
    
       
                
