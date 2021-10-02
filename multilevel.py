#MULTILEVEL INHERITANCE----The child class acts as a parent class for another child class



###MULTILEVEL INHERITANCE

class Parent:
    def func1(self,name,salary):
        self.name=name
        self.salary=salary
        print("My name is :"+self.name+" my salary is :"+str(self.salary)+" and my age is :"+str(d.age))

class Parent1(Parent):
    def savi(self,friend,age):
        self.friend=friend
        self.age=age
        print(self.friend +" is my bestiee and her age is "+str(age))
class Child(Parent1):
    def func2(self):
        print("This is function 2")

d=Child()
d.age=20
d.func1("savina",350000)
d.savi("yashu",21)
