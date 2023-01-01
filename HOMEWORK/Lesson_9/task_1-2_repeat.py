# ____________________________________________
# Date: 22.12.2022 17:32
# _____________________________________________
# Написать класс Car  и Taxi

class Car(object):
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'Car {self.color} count passenger {self.count_passenger_seats}.'

    class Taxi(object):
        def __init__(self, cars: list[Car]):
            self.cars = cars

        def find_car(self, count_passenger: int, is_baby: bool) -> Car | None:
            if is_baby:
                cars = list(filter(lambda x: not x.is_busy and x.is_baby_seat, self.cars))
            else:
                cars = list(filter(lambda x: not x.is_busy, self.cars))
            for car in cars:
                if car.count_passenger_seat >= count_passenger:
                    car.is_busy = True
                    return car
