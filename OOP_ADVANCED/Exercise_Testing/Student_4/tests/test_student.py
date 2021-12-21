from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student(name="Test", courses=None)

    def test_chek_constructor(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_add_empty_list(self):
        expected = "Course has been added."
        actual = self.student.enroll("Course_test", "test_not", "W")
        self.assertEqual(expected, actual)
        expected_keys = []
        actual_keys = self.student.courses["Course_test"]
        self.assertEqual(expected_keys, actual_keys)

    def test_enroll_chek_if_course_name_in_courses(self):
        self.student = Student('Test', {"Course_test": []})
        self.assertEqual("Course already added. Notes have been updated.", self.student.enroll("Course_test", 'Test_note'))
        expected_keys = 'Test_note'
        actual = ''.join(self.student.courses["Course_test"])
        self.assertEqual(expected_keys, actual)

    def test_add_course_notes(self):
        i = 0
        for courses_not in ["Y", ""]:
            current_courses = ["Course_test", "Course_name"]
            expected = "Course and course notes have been added."
            actual = self.student.enroll(current_courses[i], "Test_note", courses_not)
            self.assertEqual(expected, actual)
            expected_keys = 'Test_note'
            actual = ''.join(self.student.courses[current_courses[i]])
            self.assertEqual(expected_keys, actual)
            i += 1

    def test_add_note(self):
        self.student = Student('Test', {"Course_test": []})
        self.assertEqual("Notes have been updated", self.student.add_notes("Course_test", 'append note'))
        expected_keys = 'append note'
        actual = ''.join(self.student.courses["Course_test"])
        self.assertEqual(expected_keys, actual)

    def test_add_note_return_raise(self):
        self.student = Student('Test', {"Course_test": []})
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("test", 'append note')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student = Student('Test', {"Course_test": []})
        self.assertEqual("Course has been removed", self.student.leave_course("Course_test"))
        expected_keys = ''
        actual = ''.join(self.student.courses)
        self.assertEqual(expected_keys, actual)

    def test_leave_course_return_raise(self):
        self.student = Student('Test', {"Course_test": []})
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("test")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()