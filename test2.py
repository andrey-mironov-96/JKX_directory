class test_data_2(object):

    def __init__(self):
        self.data_test2_float: float = 0
        self.data_test2_str: str = 0
        self.data_test2_int: int = 0

    def input_data_test2(self):
        self.data_test2_float = float(input("data_test2_float"))
        self.data_test2_str = str(input("data_test2_str"))
        self.data_test2_int = int(input("data_test2_int"))