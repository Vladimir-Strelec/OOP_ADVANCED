from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("student_name", 11)

    def test_initialization(self):
        self.assertEqual("student_name", self.student.student_name)
        self.assertEqual(11, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_setter_name(self):
        with self.assertRaises(ValueError) as ex:
            self.student = StudentReportCard("", 11)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_valid_error_message(self):
        for num in [0, -21]:
            with self.assertRaises(ValueError) as ex:
                self.student = StudentReportCard("student_name", num)
            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_hz(self):
        for num in [13, 21]:
            with self.assertRaises(ValueError) as ex:
                self.student = StudentReportCard("student_name", num)
            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_dict(self):
        self.student.add_grade("subject", 5)
        self.assertEqual(5, self.student.grades_by_subject["subject"][0])

    def test_dict_append_in_dict(self):
        self.student.add_grade("subject", 5)
        self.student.add_grade("subject", 5)
        self.assertEqual({"subject": [5, 5]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.add_grade("subject", 5)
        self.student.add_grade("subjec", 5)
        expected = f"subject: {5:.2f}\nsubjec: {5:.2f}"
        actual = self.student.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade("subject", 5)
        self.student.add_grade("subjec", 5)
        self.student.add_grade("subjec", 5)
        expected = f"Average Grade: {5 :.2f}"
        actual = self.student.average_grade_for_all_subjects()
        self.assertEqual(expected, actual)

    def test_repr(self):
        self.student.add_grade("subject", 5)
        self.student.add_grade("subjec", 5)
        self.student.add_grade("subjec", 5)
        expected = f"Name: {self.student.student_name}\n" \
                   f"Year: {self.student.school_year}\n" \
                   f"----------\n" \
                   f"{self.student.average_grade_by_subject()}\n" \
                   f"----------\n" \
                   f"{self.student.average_grade_for_all_subjects()}"
        actual = repr(self.student)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()

