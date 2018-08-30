class user_data(object):
    def __init__(self):
        self.area_home:float = 41.0
        self.tarif_area_home:float = 17.0 #Тариф на содержание жилья
        self.tarif_HVC_home:float = 13.65
        self.tarif_el_home:float = 3.55
        self.tarif_repair_home:float = 7.0
        self.subtotal:float = 0.0

    # method of adding housing space
    def __input_area_home(self):
        while (True):
            try:
                return float(input("Площадь жилья: "))
            except:
                continue



    # method of adding a tariff for cold water the maintenance of housing
    def __input_tarif_area_home(self):
        while (True):
            try:

                print("Тариф на содержание жилья (по умолчанию", self.tarif_area_home, "):", end=' ')
                return float(input())
            except:
                continue

    #method of adding data for the maintenance of common property
    def __input_HVC_home(self):
        while (True):
            try:
                print("Тариф ХВС на содержание общего имущества МКД (по умолчанию", self.tarif_HVC_home, end="): ")
                return  float(input())
            except:
                continue

    #the tariff for the electric power of the maintenance of the general habitation
    def __input_tarif_el_home(self):
        while (True):
            try:
                print("Тариф эл. эн. на содержание обшего имущества МКД (по умолчанию", self.tarif_el_home, end="): ")
                return float(input())
            except:
                continue

    #method of adding a tariff for housing repairs
    def __input_tarif_repair_home(self):
        while(True):
            try:
                print("Тариф ремонт жилья (по умолчанию", self.tarif_repair_home, end="): ")
                return float(input())
            except:
                continue

    def __check_input_user_data(self):
        """return list"""
        tmp__tarif_area_home = self.__input_tarif_area_home()
        tmp_input_HVC_home = self.__input_HVC_home()
        tmp_input_tarif_el_home = self.__input_tarif_el_home()
        tmp_input_tarif_repair_home = self.__input_tarif_repair_home()

        __home_service = [] #list contains the data on services home

        #check whether the user entered data or left by default
        if(tmp__tarif_area_home != self.tarif_area_home):
            self.tarif_area_home = tmp__tarif_area_home
        if(tmp_input_HVC_home != self.tarif_HVC_home):
            self.tarif_HVC_home = tmp_input_HVC_home
        if(tmp_input_tarif_el_home !=self.tarif_el_home):
            self.tarif_el_home = tmp_input_tarif_el_home
        if(tmp_input_tarif_repair_home !=self.tarif_repair_home):
            self.tarif_repair_home = tmp_input_tarif_repair_home
        __home_service.append(self.__input_area_home())
        __home_service.append(self.tarif_area_home)
        __home_service.append(self.tarif_HVC_home)
        __home_service.append(self.tarif_el_home)
        __home_service.append(self.tarif_repair_home)

        #print(__home_service)
        return __home_service

    def return_results_entered_user_data(self):
        return self.__check_input_user_data()














