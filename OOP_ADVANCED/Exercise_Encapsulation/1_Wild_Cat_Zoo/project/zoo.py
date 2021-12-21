class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity: int):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if price > self.__budget and self.__animal_capacity > len(self.animals):
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if worker_name == i.name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        result_salary = [i.salary for i in self.workers]
        if sum(result_salary) <= self.__budget:
            self.__budget -= sum(result_salary)
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        result_money = [i.money_for_care for i in self.animals]
        if sum(result_money) <= self.__budget:
            self.__budget -= sum(result_money)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals"
        result += "\n"
        result += f"----- {len(lions)} Lions:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in lions])) + '\n'
        result += f"----- {len(tigers)} Tigers:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in tigers])) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in cheetahs]))
        return result

    def workers_status(self):
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers"
        result += "\n"
        result += f"----- {len(keepers)} Keepers:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in keepers])) + '\n'
        result += f"----- {len(caretakers)} Caretakers:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in caretakers])) + '\n'
        result += f"----- {len(vets)} Vets:"
        result += '\n'
        result += "{}".format('\n'.join([repr(i) for i in vets]))
        return result