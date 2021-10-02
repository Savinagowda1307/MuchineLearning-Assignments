##Hierarchial inheritance--A one parent  class contains more than one child class.






class one:
    def display(self):
        self.x=1000;
        self.y=2000;
        print("This is the method in class one");
        print("Value of X= ",self.x);
        print("Value of Y= ",self.y);
class two (one):
    def add(self):
        print("This is the method in class two");
        print("X+Y= ",(self.x+self.y));
class three(one):
    def mul(self):
        print("This is the method in class three");
        print("X*Y= ",(self.x * self.y));
t1=two();  
t2=three();  
t1.display();
t2.display();
t1.add();    
t2.mul();
