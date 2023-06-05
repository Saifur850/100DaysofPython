class Animal():
    def __init__(self):
        self.no_of_eyes= 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.no_of_nose=1
    def breathe(self):
        super().breathe()
        print("Doing this under water")
    def move(self):
        print("Move in water")

rubayet= Animal()
rubayet.breathe()