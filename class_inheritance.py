class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("I am inhaling and exhaling underwater.")
    def swim(self):
        print("Hello I am under water. Please save me.Ouhhooooo")

dory = Fish()
dory.breathe()
print(dory.num_eyes)
dory.swim()