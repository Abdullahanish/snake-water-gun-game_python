import random
#for playing agian again 
while True:
    #for error handling 
    try:

     computer =random.choice([1,0,-1])
     print(" Enter  the choice (s) for sanke , (g) for gun, (w) for water")
     # input from user 
     youstr=input("Enter your choice = ")
    except ZeroDivisionError:
      print("wrong number ")
    except ValueError:
     print("chosen value is wrong please selctect from shown one option")
     youdict={"s":1,"g":0,"w":-1}
     reversedict={1:"s",0:"g",-1:"w"}
     you=youdict[youstr]
     print(f"you chose {reversedict[you]}\n computer chose {reversedict[computer]}")

     if(computer==you):
       print("its a draw !")
     else:
      if(computer==1 and you==0):
        print("you win ")
      elif(computer==0 and you==1):
        print("computer win ")
      elif(computer==-1 and you==1):
        print("you win ")
      elif(computer==1 and you==-1):
        print("you lose ")
      elif(computer==-1 and you==0):
        print("you lose ")
      elif(computer==0 and you==-1):
        print("you win ")
      else:
        print("something wents wrong let the programmer check !")
        #error handling

    except Exception as e:
      print("somethikng wents wrong ")
