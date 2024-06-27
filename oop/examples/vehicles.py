# Vytvor triedu Vehicle, z ktorej budeme vytvarat pomocou dedicnosti nasledovne triedy:
# - Motorcycle
# - Car
# - Bus
#
# Vehicle ma napriklad atributy
# - brand
# - model
# - color
# - number_of_wheels
# - max_speed - bude definovane natvrdo pre autobusy
# - seat_capacity
#
# metody definovane v triede Vehicle:
# - start (nieco vypise)
# - get_color (vypise farbu)
# - is_possible_to_reach(speed) (vrati True alebo False podla toho, ci moze vehicle dosiahnut zadanu rychlost)

# Na zaver vytvor kratku ukazku, kde si vytvoris objekty a zavolas na ne metody.


class Vehicle:
    def __init__(
        self, brand, model, color, number_of_wheels, max_speed, seat_capacity
    ):
        self.brand = brand
        self.model = model
        self.color = color
        self.number_of_wheels = number_of_wheels
        self.max_speed = max_speed
        self.seat_capacity = seat_capacity

    def __str__(self):
        return f'{self.color} {self.brand} {self.model}'

    def start(self):
        print(f'Starting {self}')

    def get_color(self):
        print(self.color)

    def is_possible_to_reach(self, speed):
        return 0 <= speed <= self.max_speed


class Car(Vehicle):
    def __init__(
        self, brand, model, color, max_speed, seat_capacity
    ):
        super().__init__(brand, model, color, 4, max_speed, seat_capacity)


class Motorcycle(Vehicle):
    def __init__(
        self, brand, model, color, max_speed, seat_capacity
    ):
        super().__init__(brand, model, color, 2, max_speed, seat_capacity)


class Bus(Vehicle):
    MAX_SPEED = 110

    def __init__(
        self, brand, model, color, number_of_wheels, seat_capacity
    ):
        super().__init__(brand, model, color, number_of_wheels, self.MAX_SPEED, seat_capacity)


class CarCompany:
    def __init__(self):
        self.vehicle_list: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle_list.append(vehicle)

    def show_vehicles(self):
        for vehicle in self.vehicle_list:
            print(vehicle)
        print(f"Total vehicles:", len(self.vehicle_list))

    def calculate_wheels(self):
        wheel_counter = 0
        for vehicle in self.vehicle_list:
            wheel_counter += vehicle.number_of_wheels

        return wheel_counter

    def calculate_seats(self):
        seat_counter = 0
        for vehicle in self.vehicle_list:
            seat_counter += vehicle.seat_capacity

        return seat_counter


if __name__ == "__main__":
    porsche = Car('Porsche', '911', 'black', 293, 2)
    porsche.start()
    porsche.get_color()
    print(porsche.is_possible_to_reach(-15))
    print(porsche.is_possible_to_reach(200))
    print(porsche.is_possible_to_reach(300))

    school_bus = Bus('School', 'bus', 'yellow', 6, 52)
    school_bus.start()
    school_bus.get_color()
    print(school_bus.is_possible_to_reach(0))
    print(school_bus.is_possible_to_reach(90))
    print(school_bus.is_possible_to_reach(200))
    print(school_bus.is_possible_to_reach(300))

    motorbike = Motorcycle('Yamaha', 'pw50', 'blue', 250, 2)
    motorbike.start()

    print(), print(), print()
    the_best_car_company = CarCompany()
    the_best_car_company.add_vehicle(porsche)
    the_best_car_company.add_vehicle(school_bus)
    the_best_car_company.add_vehicle(motorbike)
    the_best_car_company.show_vehicles()
    print(the_best_car_company.calculate_wheels())
    print(the_best_car_company.calculate_seats())
