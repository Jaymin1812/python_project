print(""" 
===========================================
            Car For Rent Project 
=========================================== 
      """)
class carshop:

    def __init__(self,stock):
        self.stock=stock
    def displaycars(self):
        print("Total Cars:-",self.stock)
    def colors(self,*num):
        self.num=num
        return {num}
    def rentforcar(self,quntity):
        if quntity<=0:
            print("Enter the positive value or greater then Zero ")
        elif quntity>self.stock:
            print("Enter the Value (less then stock)")
        else:
            self.stock=self.stock-quntity
            print("Total Price:-",quntity*500)
            print("Total Cars:-",self.stock)

    def selectcar(self,car):

        if car=='BLACK':
            print("Price of Black Colur Car is 15,000")
        elif car=='WHITE':
            print("Price of White Colur Car is 10,000")
        elif car=='RED':
            print("Price of Red Car is 8000")
        elif car=='SILVER':
            print("Price of White Silver Car is 9000")
        elif car != "BLACK" or "WHITE" or "RED" or "SILVER":
            print("Pleace Chek Your Avalible Cars colour") 

    def availableservice(self,*city):
        self.city=city
        return{city}
    
# class total():

#     def totalrent(self,quntity):
#           self.quntity=quntity
#     for quntity in i:
#           if quntity == 'BLACK':
#               print('Black Price :-',quntity*15000)
#           elif quntity== 'WHITE':
#                  print('White Price :-',quntity*10000)
#           elif quntity== 'RED':
#                  print('Red Price:-',quntity*8000)
#           elif quntity=='SILVER':
#                  print('Silver Price:-',quntity*9000)
#           else:
#                  print('Pleace Chek Your Cars Details')
                 
while True:
    obj=carshop(50)
    # store=total()
    uc=int(input
    
    ('''
     1. Display Stocks\n
     2. Rent a Cars\n
     3. Available Colors \n
     4. Available colors For Cars And it's Price\n
     5. Our Services Available City's\n  
     6. Exit
     '''))
    
    if uc==1:
        obj.displaycars()

    elif uc==2:
        n=int(input('Enter The Qty:-----'))
        obj.rentforcar(n)

    elif uc==3:
        col=obj.colors('Black','White','Red','Silver')
        print(col)

    elif uc==4:
        select=str(input('Select Your Colore:--')).upper()
        obj.selectcar(select)

    elif uc==5:
        available=obj.availableservice('Vadodra','Ahmadabad','Rajkot','Surat','Gandhinagar')
        print(available)
    
    # elif uc==6:
    #     data=int(input('Enter Quntyty:-'))
    #     store.totalrent(data)

    else:
        break

