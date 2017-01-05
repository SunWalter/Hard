# define the class and the partent class is inherit from object
class Parent(object):

    def altered(self): #the first parameter must be self
        print ("I am implying my child")
 # Define the class Child which inherit from Parent
class Child(Parent):

    def altered(self): # the firsy parameter must be self and the second parameter you can define it by yourself
        print ("I am overriding my father ----- before ----and")
        super(Child, self).altered()
        print ("I am overriding my father ----- after -----and")


#实例化
father = Parent()
son = Child()


# using the function in class by instance as the parameter.(function name)
father.altered()
# when there are two parameter in the functoin in class you have to input only the second and so on
son.altered()
