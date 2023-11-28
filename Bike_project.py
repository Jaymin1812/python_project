print(""" 
===========================================
            Bike For Rent Project 
=========================================== 
      """)

class bikeshop:

    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bikes",self.stock)
    def rentforbike(self,q):

        if q<=0:
            print("Enter the positive value or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total price:-",q*100)
            print("Total Bikes:-",self.stock)

while True:
    obj=bikeshop(200)
    uc=int(input
    ('''
    1. Display stocks\n
    2. Rent a Bike\n
    3. Exit\n
                 ''')
                 )
    if uc ==1:
        obj.displaybike()
    elif uc ==2:
        n=int(input('Enter The Qty:------'))
        obj.rentforbike(n)
    else:
        break