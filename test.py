class Car:
    runs = True
    nbr_wheels = 4

    def __init__(self, name):
        self.name = name
        print(f"{name} was created")

    def start(self):
        if(self.runs):
            print(f"{self.name} car was running")
        else:
            print(f"{self.name} car was not runnning")

    def __str__(self):
        return f"car name : {self.name}, is running? {self.runs}"


    @classmethod
    def get_nbr_wheels(cls):
        return cls.nbr_wheels


ccc = Car("c3")
print(ccc)
# print(Car.get_nbr_wheels())
