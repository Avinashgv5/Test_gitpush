class car:
    def __init__(self,body, engin,tyre):
        self.body=body
        self.engin=engin
        self.tyre=tyre

    def milage(self):
        print("milage of this car")

class tata(car):
    pass

t= tata("solid","v6","radial")
print(t.milage())

