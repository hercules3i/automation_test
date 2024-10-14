class Bom:
    def __init__(self):
        self.work_order = ""
        self.shift = ""
        self.machines = list()
        self.workers = list()
        self.in_or_out = None
        self.warehouse_in = Warehouse()
        self.warehouse_out = Warehouse()


class Warehouse:
    def __init__(self):
        self.input = self.__Input()
        self.output = self.__Output()

    class __Input:
        def __init__(self):
            self.type = "Đầu vào"
            self.product_list = list()

    class __Output:
        def __init__(self):
            self.type = "Đầu ra"
            self.product_list = list()

    class Product:
        def __init__(self):
            self.name = ""
            self.quantity = 0
            self.unit = ""
            self.specification = ""
            self.tail = ""
            self.not_good = ""

        def IsNone(self) -> bool:
            if (self.name is None
                    and self.quantity is None
                    and self.unit is None
                    and self.specification is None
                    and self.tail is None):
                return True

            else:
                return False
