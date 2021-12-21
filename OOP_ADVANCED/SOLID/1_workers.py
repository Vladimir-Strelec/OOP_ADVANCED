from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class EatMixin(ABC):
    def eat(self):
        raise NotImplementedError()


class Worker(AbstractWorker, EatMixin):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Worker):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        for el in worker.__class__.__mro__:
            if 'Worker' in el.__name__:
                self.worker = worker
                break
        else:
            raise AssertionError("`worker` must be of type {}".format(AbstractWorker))

    def manage(self):
        if self.worker is not None:
            return self.worker.work()


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker):
    def work(self):
        print("I'm a robot. I'm working....")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()
robot = Robot()
manager.set_worker(robot)
manager.manage()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

# Може би eat да не е abstracten в бащиния клас. Също може да се създадат два отделни класа, един абстрактен с work и втори наследяващ първия и разширяващ с eat

