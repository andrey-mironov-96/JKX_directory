class user_data(object):
    def __init__(self):
        self.area_home:float = 41.0
        self.tarif_area_home = 17.0 #Тариф на содержание жилья
        self.tarif_HVC_home = 13.65
        self.tarif_el_home = 3.55
        self.tarif_repair_home = 7.0
        self.subtotal = 0.0

    def __input_area_home(self):
        while (True):
            try:
                return float(input("Площадь жилья: "))
            except:
                continue



    def __input_tarif_area_home(self):
        while (True):
            try:

                print("Тариф на содержание жилья (по умолчанию", self.tarif_area_home, "):", end=' ')
                return float(input())
            except:
                continue

    def __input_HVC_home(self):
        while (True):
            try:
                print("Тариф ХВС на содержание общего имущества МКД (по умолчанию", self.tarif_HVC_home, end="): ")
                return  float(input())
            except:
                continue

    def __input_tarif_el_home(self):
        while (True):
            try:
                print("Тариф эл. эн. на содержание обшего имущества МКД (по умолчанию", self.tarif_el_home, end="): ")
                return float(input())
            except:
                continue

    def __input_tarif_repair_home(self):
        print("Тариф ремонт жилья (по умолчанию", self.tarif_repair_home, end="): ")
        self.tarif_repair_home = input()

    def input_user_data(self):
        #self.__input_area_home()
       # self.__input_tarif_area_home()
        #self.__input_HVC_home()
        #self.__tarif_el_home()
        #self.__input_tarif_repair_home()
        self.__check_input_user_data()

    def __check_input_user_data(self):
        tmp__tarif_area_home = self.__input_tarif_area_home()
        tmp_input_HVC_home = self.__input_HVC_home()
        tmp_input_tarif_el_home = self.__input_tarif_el_home()
        tmp_input_tarif_repair_home = self.tarif_repair_home()





q1 = user_data()
q1.input_user_data()






