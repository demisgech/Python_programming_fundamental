class Person:

    def __init__(self,first_name,last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_full_name(self):
        return F"{self.__first_name} {self.__last_name}"

    def show_name(self):
        print(self.get_full_name())

person = Person("Demis","Getachew")
person.set_first_name("Eyosiyas")
person.set_last_name("Gezahegn")
first_name = person.get_first_name()
print(first_name)
person.show_name()