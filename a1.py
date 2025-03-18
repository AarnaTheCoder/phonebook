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

def add_contact(pb):
        dip=[]
        for i in range(len(pb[0])):
                if i==0:
                        dip.append(str(input("enter name")))
              
        
                if i==1:        
                         dip.append(str(input("enter number")))
                if i==2:        
                         dip.append(str(input("enter email address")))
                
                if i==3:        
                         dip.append(str(input("enter date of birth(MM/DD/YY)")))

                if i==4:        
                         dip.append(str(input("enter category(family/friends/work/other)")))

        pb.append(dip)
        return pb
def remove_existing(pb):
        input("please enter the name of the conatct you wih to remove")
        temp=0
        for i in range(len(pb)):
                print("this query  has now been removed")
                return pb
        if temp==0:
                print("sorry you have an invalid query.\nplease recheck and try again later")
                return pb

        
def delete_all(pb):
        return pb.clear
def display_all(pb):
        if not pb:
                print("list is empty[]")
        else:
                for i in range(len(pb)):
                        print(pb[i])
def thanks():
        print("thank you for using our Smartphoen directory system")
        print("please visit us again")
        sys.exit("Goodbye have a nice day!")

print("hello,welcome to your smartphone directory system")
print("you may now proceed to explore this directory")

ch=1
pb=initial_phonebook()
while ch in(1,2,3,4):
        ch=menu()
        if ch==1:
                pb=add_contact(pb)
        elif ch==2:
                pb=remove_existing(pb)
        elif ch==3:
                pb=delete_all(pb)
       
        elif ch==4:
                display_all(pb)       
        else:
                thanks()





                






                                  
                              


          
          