# if the word contains atlest 3 charctes, remove the first letter and appendd it at the end. Now append three random charcters at the starting and the end.
#     else:
#         Simply reverse the string

# Decoding:
#     if the word contains less than 3 charctes reverse it 
#     else: 
#     remove 3 random charcters from start and end. Now remove the last letter and append it to the biginning 

# your program should ask whether you want to code or decode
import random as ra
import string

code=input("Enter the Code: ")
coding=code.split(" ")
decision=int(input("Press 1 for Encoding and 2 for Decoding: "))
# For Encoding
if(decision==1):
    # Enter_encoding=int(input("Enter key from 1 to 10: "))
    listing=[]
    for i in coding:
        if(len(i)>=3):
            # clr1=mkdir[2]
            ran1="sdf"
            ran2="lph"
            # final=ran1+i[1:]+i[0]+ran2
            code1=" ".join(ra.choices(string.ascii_lowercase))
            code2=" ".join(ra.choices(string.ascii_lowercase))
            code3=" ".join(ra.choices(string.ascii_lowercase))
            code4=" ".join(ra.choices(string.ascii_lowercase))
            code5=" ".join(ra.choices(string.ascii_uppercase))
            code6=" ".join(ra.choices(string.ascii_lowercase))
            extrafinal=code1+code2+code3+i[1:]+i[0]+code4+code5+code6
            # mkdir=listing.append(final)
            # print(final)
            print(extrafinal)
            # print(mkdir)
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
    # Enter_decoding=int(input("Enter key from 1 to 10: "))
    # if(Enter_encoding==Enter_decoding):
        listing=[]
        for i in coding:
            if(len(i)>=3):
                # clr1=mkdir[2]
                ran1="sdf"
                ran2="lph"
                final=i[3:-4]             
                tilt=i[-4:]               
                tilting=tilt[:1]
                # print(tilting)
                wahaha=tilting+final
                print(wahaha)
                # mkdir=listing.append(final)
                # print(final)
                # print(mkdir)
                
            elif(len(i)==2):
                make=i[1]+i[0]
                print(make)
            else:
                ran3="ioc"
                ran4="thn"
                final=i[3:-4]
                print(final)
    # else:
    #     raise KeyError ("Key does not matched:")
else:
    print("Wrong input!")




