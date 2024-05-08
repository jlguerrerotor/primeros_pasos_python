### Classes ###

class MyEmptyPerson:
    pass # define una clase vacía. Evita el error

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias") -> None: # Contructor de clase
        self.__name = name # self.xxxx es una propiedad. Si le poinemos __xxxx delante, la propiedad es privada.
        self.__surname = surname
        self.fullname = f"{name} {surname} ({alias})"
    
    def caminar(self):
        print(f"{self.fullname} está caminando")
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

my_person = Person("Joan Lluís", "Guerrero Torta")
# print(f"{my_person.name} {my_person.surname}")
print(my_person.fullname)
my_person.caminar()

my_other_person = Person("Joan Lluís", "Guerrero Torta", "J.L.")
print(my_other_person.fullname)
my_other_person.caminar()

my_other_person.fullname = "Héctor de León (El loco de los perros)" # Puedo modificar una propiedad del objeto
print(my_other_person.fullname)
# print(my_other_person.__name) # AttributeError: 'Person' object has no attribute 'name'
my_other_person.set_name("Joan Lluís LLLL") # Setter
print(my_other_person.get_name()) # Getter