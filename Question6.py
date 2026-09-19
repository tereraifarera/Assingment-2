class Vehicle:
    """Base class with methods that subclasses can inherit or override."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):

        return f"The {self.brand} {self.model} is starting."

    def wheels(self):
        return 0

    def describe(self):

        return f"{self.brand} {self.model} ({self.wheels()} wheels)"


class Car(Vehicle):
    def __init__(self, brand, model, doors=4):
        super().__init__(brand, model)  # reuse the parent's initializer
        self.doors = doors

    def wheels(self):
        return 4

    def start(self):
        return super().start() + " Engine started with a key turn. Vroom!"


class Bike(Vehicle):

    def wheels(self):
        return 2

    def start(self):
        return f"The {self.brand} {self.model} starts moving. Pedal away!"


def main():
    vehicles = [ Vehicle("Generic", "Machine"),
                   Car("Mercedes-Benz", "GLE"),
                    Bike("Trek", "Marlin"),]

    for v in vehicles:
        print(v.describe())
        print("  ", v.start())

    print()
    car = Car("Honda", "Civic", doors=2)
    print(f"Car doors: {car.doors}")
    print(f"Is Car a Vehicle? {isinstance(car, Vehicle)}")
    print(f"Method resolution order: {[c.__name__ for c in Car.__mro__]}")


if __name__ == "__main__":
    main()