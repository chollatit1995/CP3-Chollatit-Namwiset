class Vehice:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAir(self):
        print("Turn On : Air")
class Car(Vehice):
    def sunruff(self):
        print("Open : Sunruff")

class Pickup(Vehice):
    pass

class Van(Vehice):
    pass

class EstateCar(Vehice):
    pass

car1 = Car()
car1.turnOnAir()
# car1.sunruff()

pickup1 = Pickup()
pickup1.turnOnAir()

van1 = Van()
van1.turnOnAir()

estateCar1 = EstateCar()
estateCar1.turnOnAir()