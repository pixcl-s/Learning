from unittest import TestCase

from student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.test_student_courses = Student("Pesho", {"JS": ["a", "b", "c"],
                                                 "C#": []})
        self.test_student = Student("Dobri")

    def test_init(self):
        self.assertEqual("Pesho", self.test_student_courses.name)
        self.assertEqual({"JS": ["a", "b", "c"], "C#": []}, self.test_student_courses.courses)

        self.assertEqual("Dobri", self.test_student.name)
        self.assertEqual({}, self.test_student.courses)

    def test_enroll_with_existing_course(self):
        result = self.test_student_courses.enroll("JS", ["d", "e"])

        self.assertEqual(["a", "b", "c", "d", "e"], self.test_student_courses.courses["JS"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_adding_course_and_notes(self):
        result = self.test_student.enroll("JS", ["a"], "Y")

        self.assertEqual({"JS": ["a"]}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", result)

        result = self.test_student.enroll("Python", ["a", "b"])

        self.assertEqual({"JS": ["a"], "Python": ["a", "b"]}, self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_adding_only_course(self):
        result = self.test_student.enroll("Python", ["a", "b"], "lmao")

        self.assertEqual({"Python": []}, self.test_student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_when_signed_to_course(self):
        result = self.test_student_courses.add_notes("JS", "d")

        self.assertEqual({"JS": ["a", "b", "c", "d"], "C#": []}, self.test_student_courses.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_when_not_in_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("Python", "a")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_signed_to_course(self):
        result = self.test_student_courses.leave_course("JS")

        self.assertEqual({"C#": []}, self.test_student_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_when_not_in_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("JS")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
