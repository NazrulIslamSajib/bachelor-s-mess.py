#print("**************************************Welcome To the subatash mass****************************************") 
#4
# print("Bismillah Hirahmanir Rahim")
#x=int(input())
#color ( text = "bright white" , bg = "black" , delay = 0.67 ,repeat = -1 , dict = {} )
print("\n")
print("......................Welcome To our Bachelor's software............................")

print("\n\n")


print("....................Please Enter Your Password :.........................")
d=int(1)
f=0
while 1:
 name=str(input())
 d=d+1
 if name=="sajib":
  f=1
  
 
  def menu():
    print("Enter 1 to Login                               :")
    print("Enter 2 to know the owner of the this Software :")
    print("Enter 3 to Exit                                :")
    
  menu()
  lst = []
  x=int(input())
  if x==1:
    member=int(input("How many members in your mess: "))
    print("Write down their name :")
    for i in range(0,member):
       print(i+1,end=" ")
       value=str(input())
       lst.append(value) # adding the element
    print(".......AND THESE NAME ARE...................")
    for i in range(0,member):
        print(i+1,end=" ")
        print(lst[i])


    #cost=int(input("Total cost in this month: "))
    #mill=int(input("Total mill   :"))
    
    #print("So the mill rate will be ") 
    #y=float((cost)/mill)
    #'The value is: %.3f'%num
    #print(round(y,5))
    print(".........................Bazar cost of every members:................................................")
    bzr=[]
    cost=0
    for i in range(0,member):
       print(i+1,lst[i],end=" : ")
       bazar=int(input())
       bzr.append(bazar)
       cost=cost+bzr[i]
    print("Total Cost of bazar :",end=" ")
    print(cost)
    print("Then The each person mill are  :")
    lst1=[]
    mill=0
    for i in range(0,member):
       print(i+1,lst[i],end=" :")
       value1=int(input())
       lst1.append(value1) # adding the element
       mill=mill+lst1[i]
    print("Total mill : ",end=" ")
    print(mill)
    y=float(cost/mill)
    print("So the mill rate will be :",end=" ")
    print(round(y,5))
    print("\n")
    vuya=int(input("Enter the vuya bill :")) 
    
    print(".......................Final result of all members.....................................................")
    for i in range(0,member):
        z=float((bzr[i]-(vuya+(y*lst1[i]))))
        if z>0:
         print("This member will get from the mess :",end=" ")
         print(i+1,lst[i],round(z,4))
        else:
          print("The mess will get from That member:",end=" ")
          print(i+1,lst[i],round(z,4))

  
 
  elif x==3:
    print("Bye bye for today")
  elif x==2:
    print("Hey this is sajib . I'm the owner of this application . I'm a student of IIUC . I'm 23 years old")
  elif d>10:
    print("You had submmit many times,Please wait for a 1 years ")
    break 
 elif f==1:
    break
 else:
    print("Wrong Password !!")

#print("OK bye")
xx=input()
    
