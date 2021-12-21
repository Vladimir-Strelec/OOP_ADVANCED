from unittest import TestCase, main

#from class_Car import Car


class TestCar(TestCase):
    def setUp(self):
        self.current_car = Car("Honda", "Civic", 1, 4)

    def test_constructor_input(self):
        self.assertEqual("Honda", self.current_car.make)
        self.assertEqual("Civic", self.current_car.model)
        self.assertEqual(1, self.current_car.fuel_consumption)
        self.assertEqual(4, self.current_car.fuel_capacity)
        self.assertEqual(0, self.current_car.fuel_amount)

    def test_make_methods_validations_get_new_result(self):
        self.current_car.make = "BMW"
        self.assertEqual("BMW", self.current_car.make)

    def test_make_methods_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_methods_validations_get_new_result(self):
        self.current_car.model = "323"
        self.assertEqual("323", self.current_car.model)

    def test_model_methods_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumtion_methods_and_returning_get_new_result(self):
        self.current_car.fuel_consumption = 2
        self.assertEqual(2, self.current_car.fuel_consumption)

    def test_fuel_consumtion_methods_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_methods_and_returning_get_new_result(self):
        self.current_car.fuel_capacity = 2
        self.assertEqual(2, self.current_car.fuel_capacity)

    def test_fuel_capacity_methods_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_and_returning_get_new_result(self):
        self.current_car.fuel_amount = 2
        self.assertEqual(2, self.current_car.fuel_amount)

    def test_fuel_amount_methods_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_methods_refuel_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_methods_refuel_and_returning_amount(self):
        self.current_car.refuel(10)
        self.assertEqual(4, self.current_car.fuel_amount)

    def test_methods_drive_and_returning_fuel_amount(self):
        self.current_car.fuel_amount = 5
        self.current_car.drive(40)
        self.assertEqual(4.6, self.current_car.fuel_amount)

    def test_methods_drive_and_returning_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.current_car.drive(40)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))



if __name__ == "__main__":
    main()