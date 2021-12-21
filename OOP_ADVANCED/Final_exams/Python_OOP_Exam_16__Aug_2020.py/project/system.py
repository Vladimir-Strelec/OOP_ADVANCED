from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if h.name == hardware_name:
                h.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
                System._software.append(h.software_components[-1])
                return
        return f"Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if h.name == hardware_name:
                h.install(LightSoftware(name, capacity_consumption, memory_consumption))
                System._software.append(h.software_components[-1])
                return
        return f"Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_info_check_obj_in_list(System._hardware, hardware_name)
        software = System.get_info_check_obj_in_list(System._software, software_name)
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([i.memory_consumption for i in System._software])} / {sum([i.memory for i in System._hardware])}
Total Capacity Taken: {sum([i.capacity_consumption for i in System._software])} / {sum([i.total_capacity - i.capacity for i in System._hardware])}
"""

    @staticmethod
    def system_split():
        for h in System._hardware:
            return f"""Hardware Component - {h.name}
Express Software Components: {sum([1 for k in h.software_components if k.software_type == "Express"])}
Light Software Components: {sum([1 for k in h.software_components if k.software_type == "Light"])}
Memory Usage: {sum([k.memory_consumption for k in h.software_components])} / {h.total_memory}
Capacity Usage: {sum([k.capacity_consumption for k in h.software_components])} / {h.total_capacity}
Type: {h.hardware_type}
Software Components: {', '.join([k.name if len(h.software_components) > 0 else 'None' for k in h.software_components])}
"""

    @staticmethod
    def get_info_check_obj_in_list(list, str_name):
        for o in list:
            if o.name == str_name:
                return o
        return f"Some of the components do not exist"