try:
    f1=open("/Users/mac13/Desktop/rrfile.txt",'r')
    x=f1.read()
    print("Reading File Content:")
    print(x)
    f1.close()
except FileNotFoundError:
    print("Error:The file 'rrfile.txt' was not found",)
    



    
        
