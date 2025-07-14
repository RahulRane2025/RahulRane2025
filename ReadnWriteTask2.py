text1=input("Enter the text to write to the file")
f1=open("/Users/mac13/Desktop/rroutput.txt",'w')
wf1=f1.write(text1)
print(wf1)
f1.close()

f1=open("/Users/mac13/Desktop/rroutput.txt",'r')
rfile=f1.read()
print(rfile)
f1.close()

text2=input("Enter the Additional text to append")
f1=open("/Users/mac13/Desktop/rroutput.txt",'a')
append_f1=f1.write(text2)
print(append_f1)

f1=open("/Users/mac13/Desktop/rroutput.txt",'r')
rfile=f1.read()
print(rfile)
f1.close()


    
        
