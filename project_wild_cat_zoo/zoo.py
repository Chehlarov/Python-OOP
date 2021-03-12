from .animal_base import AnimalBase
from .employee_base import EmployeeBase
from .lion import Lion
from .tiger import Tiger
from .cheetah import Cheetah
from .vet import Vet
from .keeper import Keeper
from .caretaker import Caretaker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price: int):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
        elif self.__animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: EmployeeBase):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            type_of_worker = type(worker).__name__
            return f"{worker.name} the {type_of_worker} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: EmployeeBase):
        prev_numbers_of_workers = len(self.workers)
        self.workers = [
            worker
            for worker in self.workers
            if worker.name != worker_name
        ]
        if prev_numbers_of_workers == len(self.workers):
            return f"There is no {worker_name} in the zoo"
        else:
            self.__workers_capacity -= 1
            return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_due = sum([w.salary for w in self.workers])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_due = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]
        NEW_LINE = "\n"
        return f'''You have {total_animals_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}'''

    def workers_status(self):
        total_workers_count = len(self.workers)
        vets = [w.__repr__() for w in self.workers if isinstance(w, Vet)]
        keepers = [w.__repr__() for w in self.workers if isinstance(w, Keeper)]
        care_takers = [w.__repr__() for w in self.workers if isinstance(w, Caretaker)]

        NEW_LINE = "\n"
        return f'''You have {total_workers_count} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(care_takers)} Caretakers:
{NEW_LINE.join(care_takers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}'''
