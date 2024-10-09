class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    # Сеттеры и геттеры для cpu
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        if cpu > 0:
            self.__cpu = cpu
        else:
            print("CPU должен быть положительным числом")

    # Сеттеры и геттеры для memory
    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        if memory > 0:
            self.__memory = memory
        else:
            print("Memory должно быть положительным числом")

    # Метод для арифметических вычислений
    def make_computations(self):
        return self.__cpu + self.__memory
    
    # Переопределение __str__
    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    # Магические методы для сравнения объектов по memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    
    # Сеттеры и геттеры для sim_cards_list
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        if len(sim_cards_list) > 0:
            self.__sim_cards_list = sim_cards_list
        else:
            print("Список SIM-карт не может быть пустым")

    # Метод для симуляции звонка
    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер SIM-карты")

    # Переопределение __str__
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    # Переопределение __str__
    def __str__(self):
        return f"SmartPhone(cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()})"


# Создаем объекты
computer = Computer(4, 16)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(6, 64, ["O!", "Beeline"])
smartphone2 = SmartPhone(8, 128, ["Megacom", "Beeline"])

# Печатаем информацию о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробуем методы каждого объекта

# Computer
print("Computations:", computer.make_computations())
computer.set_memory(32)
print("Updated computer memory:", computer.get_memory())

# Phone
phone.call(1, "+996 777 99 88 11")

# SmartPhone
smartphone1.use_gps("Бишкек")
smartphone1.call(2, "+996 555 11 22 33")

# Сравнение объектов Computer
print("Сравнение памяти:", smartphone1 > smartphone2)
