olt=0
pon=0
ont=1
allOlt=0
allPon=16
allOnt=35
file = open('output.txt','w')
choice = str(input('with ONT (1) or without ONT (2): '))
code_name= str(input('please enter code name: '))

if(choice == '1'):
    while olt<=allOlt:
        if(olt<=allOlt):
            if (olt<=allOlt):
                olt+=1
                pon=1
            while pon<=allPon:
                ont=1
                while ont<=allOnt:
                    print(f'''{code_name}-GX-OLT0{olt}:{pon}:{ont},''')
                    output=code_name+"-GX-OLT0"+str(olt)+":"+str(pon)+":"+str(ont)+","
                    file.write(output)
                    ont+=1
                pon+=1
elif(choice=='2'):
    while olt<=allOlt:
        if(olt<=allOlt):
            if (olt<=allOlt):
                olt+=1
                pon=1
            while pon<=allPon:
                print(f'''{code_name}-GX-OLT0{olt}:{pon},''')
                output=code_name+"-GX-OLT0"+str(olt)+":"+str(pon)+","
                file.write(output)
                
                pon+=1
            
        
    # if(i==1):
    #     print(i)
    #     i+=1
# i=1
# j=1
# k=1
# print(f'''SRPSRP-GX-OLT0{i}:{j}:{k}''')