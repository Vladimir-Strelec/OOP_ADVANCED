from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(fuel=5.5, horse_power= 6.6)

    def test_vehicle_initialization(self):
        self.assertEqual(5.5, self.vehicle.fuel)
        self.assertEqual(5.5, self.vehicle.capacity)
        self.assertEqual(6.6, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_return_result_fuel(self):
        self.vehicle.fuel = 13.50
        self.vehicle.drive(10)
        self.assertEqual(1.0, self.vehicle.fuel)

    def test_drive_return_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_return_result_refuel(self):
        self.vehicle.fuel = 13.50
        self.vehicle.capacity = 13.50
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(6.0, self.vehicle.fuel)

    def test_refuel_return_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_print(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} " \
                         f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()