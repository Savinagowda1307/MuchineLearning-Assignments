####SINGLE INHERITANCE------When Inheritance involves one child class and one parent class



###SINGLE INHERITANCE


class Parent:
    def func1(self,name,salary):
        self.name=name
        self.salary=salary
        print("My name is :"+self.name+" my salary is :"+str(self.salary)+" and my age is :"+str(d.age))

class Child(Parent):
    def func2(self):
        print("This is function 2")

d=Child()
d.age=20
d.func1("savina",350000)
d.func2()
