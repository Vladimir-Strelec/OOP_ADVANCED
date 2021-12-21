from project.software.software import Software


class Hardware:
    _ERROR_MESSAGE = "Software cannot be installed"

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.total_memory = memory
        self.total_capacity = capacity

    def install(self, software: Software):
        if self.memory >= software.memory_consumption and self.capacity >= software.capacity_consumption:
            self.software_components.append(software)
            self.capacity -= software.capacity_consumption
        else:
            raise Exception(self._ERROR_MESSAGE)

    def uninstall(self, software: Software):
        self.chek_software_in_list_by_components(self.software_components, software)
        self.capacity += software.capacity_consumption

    @staticmethod
    def chek_software_in_list_by_components(software_components, software):
        for s in software_components:
            if s.name == software.name:
                software_components.remove(software)

