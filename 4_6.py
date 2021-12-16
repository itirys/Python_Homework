# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.

# 6. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse:  # Склад
    def __init__(self):
        self.warehouse_dict = {}

    def menu_warehouse(self):
        a = ''
        while a != 'q':
            print(f'{"-" * 35}\nМеню склада\n{"-" * 35}\n'
                  'Добавить на склад:\n\t1 -- принтер(ы),\n\t2 -- сканер(ы),\n\t3 -- копир. аппарат(ы)\n'
                  f'4 -- Получить со склада\n5 -- Посмотреть, что есть на складе\nq -- Выйти из программы\n{"-" * 35}')
            a = input('Выберите пункт меню: ')

            if a == 'q':
                break
            elif a.isdigit():
                if 1 <= int(a) <= 3:
                    sel = {1: Printer, 2: Scanner, 3: Copier}
                    Warehouse.add_to_warehouse(self, sel[int(a)])
                elif a == '4':
                    name = input('Наименование оборудования: ')
                    try:
                        count = int(input('Количество, шт.: '))
                    except ValueError:
                        print('Количество оборудования должно быть целым числом!')
                    else:
                        Warehouse.receive_from_warehouse(self, name, count)
                elif a == '5':
                    print(Warehouse.__str__(self))
                else:
                    print('Неверный пункт меню!')
            else:
                print('Необходимо выбрать либо "q", либо одну из цифр меню!')

    def add_to_warehouse(self, func):
        item = {}
        b = func().__dict__

        for key, value in b.items():
            if key != 'type_equipment':
                item[Equipment.interpretation[key]] = value

        if b['type_equipment'] in self.warehouse_dict.keys():
            self.warehouse_dict[b['type_equipment']].append(item)
        else:
            self.warehouse_dict[b['type_equipment']] = [item]

        print('Оборудование добавлено на склад')

    def receive_from_warehouse(self, name, count):
        i = None
        for key, value in self.warehouse_dict.items():
            for ind in range(len(value)):
                if name in value[ind]['Наименование']:
                    stock = value[ind]['Количество, шт.']
                    i = ind
                    k = key
        if stock > 0:
            if count <= stock:
                if count < stock:
                    self.warehouse_dict[k][i]['Количество, шт.'] = stock - count
                else:
                    self.warehouse_dict[k].pop(i)
                    if len(self.warehouse_dict[k]) == 0:
                        self.warehouse_dict.pop(k)
                print('Получите и распишитесь!')
            else:
                print('Такого количества нет на складе! В наличии:', stock)
        else:
            print('Такого оборудования нет на складе!')

    def __str__(self):
        all_equipment = ''
        if len(self.warehouse_dict) > 0:
            for key, value in self.warehouse_dict.items():
                all_equipment += f'\n{key}\n{"*" * 35}\n'
                for ind in range(len(value)):
                    for k, v in value[ind].items():
                        all_equipment += f'\t{k}: {v}\n'
                    if ind != (len(value) - 1):
                        all_equipment += f'\t{"-" * 31}\n'
            return all_equipment
        else:
            return 'Склад пустой!'


class Equipment:  # Оргтехника
    interpretation = {'type_equipment': 'Тип оборудования',
                      'name': 'Наименование',
                      'price': 'Стоимость, руб.',
                      'count': 'Количество, шт.'
                      }

    def __init__(self):
        item_param = {}
        while item_param == 'Error' or item_param == {}:
            item_param = Equipment.add_item()
        else:
            self.name = item_param['name']
            self.price = item_param['price']
            self.count = item_param['count']

    @staticmethod
    def add_item():
        name = input('Введите название оборудования: ')
        try:
            price = float(input('Введите его стоимость: '))
            count = int(input('Введите количество, шт.: '))
        except ValueError:
            print(f'Ошибка ввода данных!\n{"-" * 40}')
            return 'Error'
        else:
            return {'name': name, 'price': price, 'count': count}


class Printer(Equipment):
    Equipment.interpretation['technology'] = 'Технология печати'

    def __init__(self):
        self.type_equipment = 'Принтер'
        Equipment.__init__(self)
        self.technology = Printer.add_item()

    @staticmethod
    def add_item():
        technology = int(input('Укажите технологию печати (лазерная - 1, струйная - 2): '))
        return 'лазерная' if technology == 1 else 'струйная'


class Scanner(Equipment):
    Equipment.interpretation['resolution'] = 'Разрешение, dpi'

    def __init__(self):
        self.type_equipment = 'Сканер'
        Equipment.__init__(self)
        self.resolution = Scanner.add_item()

    @staticmethod
    def add_item():
        return input('Укажите разрешение сканирования: ')


class Copier(Scanner, Printer):
    def __init__(self):
        self.type_equipment = 'Копировальный аппарат'
        Equipment.__init__(self)
        self.technology = Printer.add_item()
        self.resolution = Scanner.add_item()


sklad1 = Warehouse()
sklad1.menu_warehouse()
# Будем считать, что оборудование с одинаковым наименованием добавляться не будет пока оно есть в наличии на складе ))
