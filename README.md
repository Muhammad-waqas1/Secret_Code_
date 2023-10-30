# Secret_Code_
# Rules:<br>
Encoding:<br>
if the word contains atleast 3 characters, remove the first letter and append it at the end. Now append three random charcters at the starting and at the end.<br>
else(less than 3 characters) Simply reverse the string<br>
Decoding:<br>
if the word contains less than 3 charctes reverse it.<br>
else remove 3 random characters from start and end. Now move the last letter to the start of code<br><br>

Note:Your program should ask whether you want to code or decode
```
import random as ra
import string

code=input("Enter the Code: ")
coding=code.split(" ")
decision=int(input("Press 1 for Encoding and 2 for Decoding: "))
# For Encoding
if(decision==1):
        listing=[]
    for i in coding:
        if(len(i)>=3):
            ran1="sdf"
            ran2="lph"            
            code1=" ".join(ra.choices(string.ascii_lowercase))
            code2=" ".join(ra.choices(string.ascii_lowercase))
            code3=" ".join(ra.choices(string.ascii_lowercase))
            code4=" ".join(ra.choices(string.ascii_lowercase))
            code5=" ".join(ra.choices(string.ascii_uppercase))
            code6=" ".join(ra.choices(string.ascii_lowercase))
            extrafinal=code1+code2+code3+i[1:]+i[0]+code4+code5+code6
            print(extrafinal)            
        elif(len(i)==2):
            make=i[1]+i[0]
            print(make)
        else:
            rand1=" ".join(ra.choices(string.ascii_lowercase))
            rand2=" ".join(ra.choices(string.ascii_lowercase))
            rand3=" ".join(ra.choices(string.ascii_lowercase))
            rand4=" ".join(ra.choices(string.ascii_lowercase))
            rand5=" ".join(ra.choices(string.ascii_lowercase))
            rand6=" ".join(ra.choices(string.ascii_lowercase))
            elsefinal=rand1+rand2+rand3+i[0]+rand4+rand5+rand6
            print(elsefinal)
# Decoding
elif(decision==2):
        listing=[]
        for i in coding:
            if(len(i)>=3):
                ran1="sdf"
                ran2="lph"
                final=i[3:-4]             
                tilt=i[-4:]               
                tilting=tilt[:1]
                wahaha=tilting+final
                print(wahaha)                
            elif(len(i)==2):
                make=i[1]+i[0]
                print(make)
            else:
                ran3="ioc"
                ran4="thn"
                final=i[3:-4]
                print(final)
else:
    print("Wrong input!")
```
