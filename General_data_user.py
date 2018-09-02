class General_data_user(object):


    def __init__(self):
        self.area_home:float = 0.2
        self.number_ocupants:int = 2

    def __error_add_user_data(self):
        print("Некорректные данные")



    def __add_user_data(self):
        while(True):
            try:
                self.area_home = float(input("Введите площадь жилища: "))
                self.number_ocupants = int(input("Введите количество прописанных жильцов в жилище: "))
                if(self.area_home<0 or self.number_ocupants<0):
                    self.__error_add_user_data()
                    continue
                return 0
            except:
                self.__error_add_user_data()
                continue


    def return_user_data(self):
        try:
            self.__add_user_data()
            from time import sleep
            sleep(0.9)
            print("Данные успешно обработанны")
        except:
            print("Внутреняя ошибка")

        return 0



