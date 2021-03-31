import unittest
from D21_person import Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Jordan', "J", 27)

    def test_person_is_properly_initiated(self):
        self.assertEqual(self.person.first_name, 'Jordan')
        self.assertEqual(self.person.last_name, 'J')
        self.assertEqual(self.person.age, 27)

    def test_person_full_name_is_the_combination_of_first_and_last_name(self):
        full_name = self.person.get_full_name()
        self.assertEqual(full_name, "Jordan J")


if __name__ == '__main__':
    unittest.main()
