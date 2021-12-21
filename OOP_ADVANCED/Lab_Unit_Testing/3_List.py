class IntegerList:
    def __init__(self, *args):
        self.__data = [x for x in args if type(x) == int]

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)








from unittest import TestCase, main


class List(TestCase):
    def setUp(self):
        self.list_integer = IntegerList(1, 2, 3, 4, 5)

    def test_an_element(self):
        self.assertEqual([1, 2, 3, 4, 5], self.list_integer._IntegerList__data)

    def test_add_an_element(self):
        self.list_integer.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.list_integer._IntegerList__data)

    def test_the_add_data_in_the_constructor(self):
        self.list_integer = IntegerList("a", "2")
        self.assertEqual([], self.list_integer._IntegerList__data)

    def test_add_a_string(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.add("a")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_current_index(self):
        self.list_integer.remove_index(0)
        self.assertEqual([2, 3, 4, 5], self.list_integer._IntegerList__data)

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_method_get_the_specific_element_being_returned(self):
        self.assertEqual(1, self.list_integer.get(0))

    def test_method_get_returned__index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.get(22)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_method_insert_add_element_int(self):
        self.list_integer.insert(0, 55)
        self.assertEqual(55, self.list_integer._IntegerList__data[0])

    def test_method_insert_raise_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.insert(22, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_method_insert_raise_add_string_element(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.insert(3, "a")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_method_get_returned__index(self):
        self.assertEqual(0, self.list_integer.get_index(1))

    def test_method_get_biggest(self):
        self.assertEqual(5, self.list_integer.get_biggest())


if __name__ == "__main__":
   main()


