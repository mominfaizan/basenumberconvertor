def binarytodecimal():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==2):
        validnumber=validnumber+1
        break
       elif(i==3):
        validnumber=validnumber+1
        break
       elif(i==4):
        validnumber=validnumber+1
        break
       elif(i==5):
        validnumber=validnumber+1
        break
       elif(i==6):
        validnumber=validnumber+1
        break
       elif(i==7):
        validnumber=validnumber+1
        break
       elif(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      binarytodecimal()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(2,indexx)
        x=x+1
    print(decimalnumber)
def binarytooctal():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==2):
        validnumber=validnumber+1
        break
       elif(i==3):
        validnumber=validnumber+1
        break
       elif(i==4):
        validnumber=validnumber+1
        break
       elif(i==5):
        validnumber=validnumber+1
        break
       elif(i==6):
        validnumber=validnumber+1
        break
       elif(i==7):
        validnumber=validnumber+1
        break
       elif(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      binarytooctal()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(2,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if(decimalnumber>=1):
            innerfunction(decimalnumber//8)
        print(decimalnumber % 8, end = '')
    innerfunction(decimalnumber)
def binarytohexadecimal():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==2):
        validnumber=validnumber+1
        break
       elif(i==3):
        validnumber=validnumber+1
        break
       elif(i==4):
        validnumber=validnumber+1
        break
       elif(i==5):
        validnumber=validnumber+1
        break
       elif(i==6):
        validnumber=validnumber+1
        break
       elif(i==7):
        validnumber=validnumber+1
        break
       elif(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      binarytohexadecimal()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(2,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if(decimalnumber>=1):
            innerfunction(decimalnumber//16)
        if(decimalnumber%16==10):
         print("A",end='')
        elif(decimalnumber%16==11):
         print("B",end='') 
        elif(decimalnumber%16==12):
         print("C",end='')          
        elif(decimalnumber%16==13):
         print("D",end='')           
        elif(decimalnumber%16==14):
         print("E",end='') 
        elif(decimalnumber%16==15):
         print("F",end='')
        else:
         print(decimalnumber%16,end='') 
    innerfunction(decimalnumber)
def decimaltobinary():
    def innerfunction(number):
        if number >= 1:
          innerfunction(number//2)
        print(number % 2, end = '')
    number=int(input("enter number in decimal:"))
    innerfunction(number)    
def decimaltooctal():
    def innerfunction(number):
        if(number>=1):
            innerfunction(number//8)
        print(number % 8, end = '')
    number=int(input("enter decimal number"))
    innerfunction(number)
def decimaltohexadecimal():
    def innerfunction(number):
        if(number>=1):
            innerfunction(number//16)
        if(number%16==10):
         print("A",end='')
        elif(number%16==11):
         print("B",end='') 
        elif(number%16==12):
         print("C",end='')          
        elif(number%16==13):
         print("D",end='')           
        elif(number%16==14):
         print("E",end='') 
        elif(number%16==15):
         print("F",end='')
        else:
         print(number%16,end='') 
    number=int(input("enter decimal number"))
    innerfunction(number)
def octaltobinary():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      octaltobinary()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(8,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if decimalnumber >= 1:
          innerfunction(decimalnumber//2)
        print(decimalnumber % 2, end = '')
    innerfunction(decimalnumber)
def octaltodecimal():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      octaltodecimal()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(8,indexx)
        x=x+1
    print(decimalnumber)
def octaltohexadecimal():
    number=(input("enter number in int:"))
    my_list = [int(x) for x in str(number)]
    validnumber=0
    length=len(my_list)
    for i in my_list:
       if(i==8):
        validnumber=validnumber+1
        break
       elif(i==9):
        validnumber=validnumber+1
        break
    if(validnumber>0):
      print("number is not valid enter valid number")
      octaltodecimal()
    x=0
    decimalnumber=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+i*pow(8,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if(decimalnumber>=1):
            innerfunction(decimalnumber//16)
        if(decimalnumber%16==10):
         print("A",end='')
        elif(decimalnumber%16==11):
         print("B",end='') 
        elif(decimalnumber%16==12):
         print("C",end='')          
        elif(decimalnumber%16==13):
         print("D",end='')           
        elif(decimalnumber%16==14):
         print("E",end='') 
        elif(decimalnumber%16==15):
         print("F",end='')
        else:
         print(decimalnumber%16,end='') 
    innerfunction(decimalnumber)
def hexadecimaltobinary():
    number=input("enter number in hexadecimal:")
    my_list = [str(x) for x in str(number)]
    length=len(my_list)
    for i in range(length):
     if str(my_list[i]) == 'A':
        my_list[i] = 10
     elif str(my_list[i]) == 'B':
        my_list[i] = 11
     elif str(my_list[i]) == 'C':
        my_list[i] = 12
     elif str(my_list[i]) == 'D':
        my_list[i] = 13
     elif str(my_list[i]) == 'E':
        my_list[i] = 14      
     elif str(my_list[i]) == 'F':
        my_list[i] = 15
    decimalnumber=0
    x=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+int(i)*pow(16,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if decimalnumber >= 1:
          innerfunction(decimalnumber//2)
        print(decimalnumber % 2, end = '')
    innerfunction(decimalnumber)
def hexadecimaltodecimal():
    number=input("enter number in hexadecimal:")
    my_list = [str(x) for x in str(number)]
    length=len(my_list)
    for i in range(length):
     if str(my_list[i]) == 'A':
        my_list[i] = 10
     elif str(my_list[i]) == 'B':
        my_list[i] = 11
     elif str(my_list[i]) == 'C':
        my_list[i] = 12
     elif str(my_list[i]) == 'D':
        my_list[i] = 13
     elif str(my_list[i]) == 'E':
        my_list[i] = 14      
     elif str(my_list[i]) == 'F':
        my_list[i] = 15
    decimalnumber=0
    x=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+int(i)*pow(16,indexx)
        x=x+1
    print(decimalnumber)
def hexadecimaltooctal():
    number=input("enter number in hexadecimal:")
    my_list = [str(x) for x in str(number)]
    length=len(my_list)
    for i in range(length):
     if str(my_list[i]) == 'A':
        my_list[i] = 10
     elif str(my_list[i]) == 'B':
        my_list[i] = 11
     elif str(my_list[i]) == 'C':
        my_list[i] = 12
     elif str(my_list[i]) == 'D':
        my_list[i] = 13
     elif str(my_list[i]) == 'E':
        my_list[i] = 14      
     elif str(my_list[i]) == 'F':
        my_list[i] = 15
    decimalnumber=0
    x=0
    for i in my_list:
        indexx=length-x-1
        decimalnumber=decimalnumber+int(i)*pow(16,indexx)
        x=x+1
    def innerfunction(decimalnumber):
        if(decimalnumber>=1):
            innerfunction(decimalnumber//8)
        print(decimalnumber % 8, end = '')
    innerfunction(decimalnumber)        
def choicefunction():
 print("which number system do you want to convert:")
 print("1.binary")
 print("2.decimal")
 print("3.octal")
 print("4.hexadecimal")
 choice1=int(input("enter your  choice:"))
 if(choice1==1):
    def innerchoice():
      print("which number system do you want to convert ino:")
      print("1.decimal")
      print("2.octal")
      print("3.hexadecimal")
      choice2=int(input("enter your  choice:"))
      if(choice2==1):
       binarytodecimal()
      elif(choice2==2):
       binarytooctal()
      elif(choice2==3):
       binarytohexadecimal()
      else:
       print("enter valid choice")
       innerchoice()
    innerchoice()
 elif(choice1==2):
    def innerchoice():
      print("which number system do you want to convert ino:")
      print("1.binary")
      print("2.octal")
      print("3.hexadecimal")
      choice2=int(input("enter your  choice:"))
      if(choice2==1):
       decimaltobinary()
      elif(choice2==2):
       decimaltooctal()
      elif(choice2==3):
       decimaltohexadecimal()
      else:
       print("enter valid choice")
       innerchoice()
    innerchoice()
 elif(choice1==3):
    def innerchoice():
      print("which number system do you want to convert ino:")
      print("1.binary")
      print("2.decimal")
      print("3.hexadecimal")
      choice2=int(input("enter your  choice:"))
      if(choice2==1):
       octaltobinary()
      elif(choice2==2):
       octaltodecimal()
      elif(choice2==3):
       octaltohexadecimal()
      else:
       print("enter valid choice")
       innerchoice()
    innerchoice()      
 elif(choice1==4):
    def innerchoice():
      print("which number system do you want to convert ino:")
      print("1.binary")
      print("2.decimal")
      print("3.octal")
      choice2=int(input("enter your  choice:"))
      if(choice2==1):
       hexadecimaltobinary()
      elif(choice2==2):
       hexadecimaltodecimal()
      elif(choice2==3):
       hexadecimaltooctal()
      else:
       print("enter valid choice")
       innerchoice()
    innerchoice()        
 else:
    print("enter valid choice")
    choicefunction()
choicefunction()