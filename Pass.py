for x in range (1,5000):
    
    if x % 20 == 0:
        print(f"{x} :   twist")
        
    elif x % 15 == 0:
        pass
        
    elif x % 5 == 0:
         print(f"{x} :  fizz")
    
    elif x % 3 == 0:
        print(f"{x} :  buzz")