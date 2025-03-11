import sys

def initial_phonebook():
          rows,cols=int(input("please enter iniatial number of contacts")),5

          phone_book=[]
          print(phone_book)
          for i in range(rows):
                  print("\nEnter conatct %d details in teh following order(ONLY):"%(i+1))
                  print("NOTE:* indicates mandatory fields")
                  print("....................................................................")

                  temp=[]
                  for j in range(cols):
                              if j==0:
                                  temp.append(str(input("enter name"))) 
                                  
                              if j==1:
                                        temp.append(int(input("enter number*")))
                                   
                              if j==2:
                              
                                          temp.append(str(input("enter enter email address")))
                                          if temp[j]=='' or temp[j]=="":
                                                  temp[j]=none

                              if j==3:
                                      temp.append(str(input("enter date of birth(dd/mm/yy)")))
                              if j==4:
                                      temp.append
                                      (str(input("enter category (family/friends/work/other)"))) 

                                      phone_book.append(temp) 

                                      print(phone_book)  
                                      return phone_book
def menu():
       print("\tYou can now perform teh following options on this phonebook\n ")
       print("1.add a new contact")
       print("2.remove a  contact")
       print("3.delete a  contact")
       print("4.search a contact")
       print("5.display a contact")
       print("6.exit")

       choice=int(input("please enter your choice"))
       return choice
       




                                  
                              


          
          