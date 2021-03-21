from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")


class SeniorWorker(BaseWorker):
    def work(self):
        print("I am doing senior stuff")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker: BaseWorker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
senior_worker = SeniorWorker()

manager.set_worker(senior_worker)
manager.manage()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
