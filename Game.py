import random  
import sys  
file1=open("Result3.txt","a+")
class Game:
   def _init_(self):
       print("class initialised")
   def startgame(self):
       score=0
       ques1=["Which was India’s first-ever tactical missile?"," Which type of coal is difficult to light in the open air?","Which industry was started first in India? ","Which metal is non toxic in nature?","Which is used as the logo of the World Wide Fund for Nature (WWF) ?"]
       ans1=["AGNI","PEAT","TEA","GOLD","PANDA"]
       for j in range(5,0,-1):
            x=random.randint(0,j-1)
            print(str(ques1[x]).upper())
            a=input()
            if str(a).upper() == str(ans1[x]):
                 print("YEAH!YOU ARE CORREECT!!!")
                 score=score+10
            else:
                 print("OOPS!YOU ARE WRONG!!!")

            del ques1[x]
            del ans1[x]
       file1.write(str(score)+"\n")
       print(score,end='')
   def displaydetails(self):
      name,score=checkuser()
      print("ENTER YOUR CHOICE:\n1.SHOW ALL PARTICIPANTS SCORE\n2.SHOW WINNERS\n3.EXIT") 
      choice=input()
      if choice == '' or int(choice) == 3:
         print('THANK YOU !')
         sys.exit()
      if(int(choice)==1):
         print("ALL PARTICIPANTS DETAILS")
         x=len(name)
         for i in range(0,x):
            print("NAME : "+name[i]+"\tSCORE : "+score[i])
      elif(int(choice)==2):
         print("WINNER DETAILS:")
         x=max(score)
         y=len(score)
         if int(x)>0:
            for i in range(0,y):
                if int(x)==int(score[i]):
                   print("NAME : "+name[i]+"\tSCORE : "+score[i])
         else:
            print("NO WINNERS IN THE GAME")
      else:
         print("SORRY YOU HAVE ENTERED WRONG CHOICE")
def checkuser():
      name=list()
      score=list()
      file2=open("Result3.txt","r")
      content=file2.readlines()
      content = [x.strip() for x in content]
      x=len(content)
      for i in range(0,x):
          if i%2==0:
                name.append(content[i])
          else:
                score.append(content[i])
      return name,score
s=Game()
flag="y"
temp=0
nam=list()
while flag=="Y" or flag=="y":
     print("WELCOME TO THE GAME!!!")
     Name=input("ENTER YOUR NAME:")
     name,score=checkuser()
     x=len(nam)
     for i in range(0,x):
        if str(Name).upper()==str(nam[i]):
           temp=1
     x=len(name)
     for i in range(0,x):
        if str(Name).upper()==str(name[i]):
           temp=1
           break
     if temp==1:
        print("USERNAME HAS ALREADY ATTENDED!!!TRYWITH ANOTHER NAME!")
     else:
        nam.append(Name.upper())
        file1.write(str(Name).upper()+"\n")
        s.startgame()
        print(" IS YOUR SCORE "+Name.upper())
     print("ENTER Y TO CONTINUE")
     flag=input()
     temp=0
file1.close()
flag="y"
while flag=="Y" or flag=="y":
     s.displaydetails()
     print("ENTER Y TO CONTINUE DISPLAY DETAILS OR PRESS ANYOTHER KEY TO EXIT")
     flag=input()
print("THANK YOU FOR PARTICIPATING IN THE QUIZ!!!")
