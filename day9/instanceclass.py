class car:
    wheels=4
    def __init__(self):
        self.price=500000
        self.mileage=14
c1=car()
c1.wheels=9
c1.price=100000
print(c1.price,c1.mileage,c1.wheels)
 