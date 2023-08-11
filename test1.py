class Person:
    def __init__(self,name,surname,age,year_of_birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.year_of_birth=year_of_birth
manoj_detail=Person("manoj","musale",19,2004) 
print(manoj_detail.name)
print(type(manoj_detail))       