from datetime import datetime
class Account:
    
    bank_name="Bank of India"

    def __init__(self,holder, acc,psswd,acc_type,balance):
        self.holder_name=holder
        self.account_no=acc
        self.__password=psswd # Here psswd is private we can't access outside class
        self.account_type=acc_type
        self.balance=balance

    def show_acc_details(self):
        print(f"Account Holder name: {self.holder_name}\nAccount No: {self.account_no}\nAccount type: {self.account_type}\nPrevious Balance was:{self.balance}")
        
    def credit(self,amount):
        self.balance+=amount
        date=datetime.now()
        print(f"RS {amount} was Credited\nDateTime: {date}")
        #print(f"Total Current Balnce is: {self.balance}") # OR
        print(f"Total Current Balnce is: {self.get_balance()}") # Here Calling get_balance() internal Method to get final amount
        
    def debit(self,amount):
        self.balance-=amount
        date=datetime.now()
        print(f"RS {amount} was Debited\nDateTime: {date}")
        #print(f"Total Current Balnce is: {self.balance}") # OR
        print(f"Total Current Balnce is: {self.get_balance()}") # Here Calling get_balance() internal Method to get final amount

    def get_balance(self): # Here Created Method For Get Final Balance
        #print(f"Total Current Balnce is: {self.balance}") # OR
        return self.balance

bank=Account("Raju",12345678,"exyp","Saving",2000)
print(bank.account_no) # Here We can access Acc_no bcz acc_no is not private
print(bank.__password) # Here We can,t access password bcz password is a private attribute
#bank.show_acc_details()
#bank.credit(5000)
#bank.debit(600)
#bank.credit(12000) # Here Again Credited
# del bank # we can delete object
        

'''
class Student:
    college="AMC Eng"

    def __init__(self,name,eng,hindi,math,phy,chem):
        self.name=name
        self.eng=eng
        self.hindi=hindi
        self.math=math
        self.phy=phy
        self.chem=chem
        self.total_marks=eng+hindi+math+phy+chem
        self.avg=self.total_marks/5
    def show(self):
        print(f"Name: {self.name}\nTotal Marks: {self.total_marks}\nAverage: {self.avg}")
           

obj=Student("Raju",52,60,90,78,36)
obj.show()


class Mobile:
    name="Md Raju Alam"
    age=28
    print(name,age)

    def __init__(self,n,m,c,p):
        self.name=n
        self.model=m
        self.color=c
        self.price=p

    def show(self, d):
        date=d
        print(self.name,self.model,self.color,self.price,date)

m_name=input("Enter mobile name\n")
m_model=input("Enter mobile model\n")
m_color=input("Enter mobile color\n")
m_price=int(input("Enter mobile price\n"))
m_date=input("Enter manufacturing date\n")
redme=Mobile(m_name,m_model,m_color,m_price)
redme.show(m_date)


mobile="Apple"
model="Apple2024"
color="Silver"
manuf=2020
price=150000

print(mobile,model,color,manuf,price)


def mob():
    mobile="Apple"
    model="Apple2024"
    color="Silver"
    manuf=2020
    price=150000

    print(mobile,model,color,manuf,price)

mob()


class Mobile:
    print("This is class")

    name="Sudhir"
    age=28
    print(name,age)

    def __init__(self):
        print(self)
        print(id(self))
        self.mobile="Apple"
        self.model="Apple2024"
        self.color="Silver"
        self.manuf=2020
        self.price=150000
        print("This is method")

    def show(self):
        print("This instance method")
        print(self.mobile,self.model,self.color,self.manuf,self.price)
        
nokia=Mobile()
print(nokia)
print(id(nokia))
nokia.show()
redme=Mobile()
print(redme,id(redme))
###
class Mobile:
    name="sudhir"

    def __init__(self, m,c,p):

        self.Model=m
        self.Color=c
        self.Price=p     
    def show(self):
         name="rama"
        print(f"Model of Mobile: {self.Model}\nColor:{self.Color}\nPrice of Mobile: {self.Price}")

redme=Mobile("Redme","Red",50000)
redme.show()

nokia=Mobile("Nokia","blue",3000)
nokia.show()
'''

