import unittest
from D21_worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Jordan', 100, 42)

    def test_worker_is_initialized(self):
        self.assertEqual(self.worker.name, 'Jordan')
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 42)

    def test_energy_is_increased(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, old_energy + 1)

    def test_exception_is_raised_when_working_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()
        self.worker.energy = -4
        with self.assertRaises(Exception):
            self.worker.work()

    def test_money_are_increased_after_work(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_energy_decreases_after_worker(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'Jordan has saved 0 money.')

if __name__ == '__main__':
    unittest.main()
