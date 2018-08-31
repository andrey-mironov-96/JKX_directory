class collection_of_user_data_about_home_services(object):
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

class collection_of_user_data_about_water(object):
    def __init__(self):
        # количество кубов * количество человек * тариф
        # показания счетчика * тариф
        self.__number_water_kube:float = 11
        self.__water_counter:float = 0
        self.__number_of_residents:int = 1
        self.__tarif_water:float = 16.45

        self.__cold_water:float = 0

    def __error_add_user_data(self):
        print("Введены некорректные данные")


    #number cube for man
    def __add_user_data_about_water(self):
        while(True):
            try:
                print("Введите количество кубов на человека (по умолчанию 9,86): ", end="")
                data = float(input())
                if data>0:
                    return data
                else:
                    self.__error_add_user_data()
                    continue
            except:
                self.__error_add_user_data()
                continue

    def __add_user_data_water_counter(self):
        while(True):
            try:
                print("Количество кубов в прошлом месяце: ",end="")
                last_month = float(input())
                if last_month < 0:
                    self.__error_add_user_data()
                    continue

                print("Количество кубов в текущем месяце: ",end="")
                current_month = float(input())
                if current_month < 0:
                    self.__error_add_user_data()
                    continue

                if(last_month>current_month):
                    self.__error_add_user_data()
                    continue

                number_kube:float = current_month-last_month
                return number_kube
            except:
                self.__error_add_user_data()
                continue

    def __add_user_data_number_of_residents(self):
        while(True):
            try:
                print("Введите количество людей прописанных в жилье: ",end="")
                data = int(input())
                if data > 0:
                    return data
                else:
                    self.__error_add_user_data()
                    continue
            except:
                self.__error_add_user_data()
                continue

    def __add_user_data_tarif_water(self):
        while(True):
            try:
                print("Введите тариф на воду (по  умолчанию 135.73): ",end="")
                data = float(input())
                if data>0:
                    return data
                else:
                    self.__error_add_user_data()
                    continue
            except:

                self.__error_add_user_data()
                continue

    def __check_water(self):
        tmp_data_about_water = self.__add_user_data_about_water()
        tmp_data_water_counter = self.__add_user_data_water_counter()
        tmp_data_number_of_residents = self.__add_user_data_number_of_residents()
        tmp_data_tarif_water = self.__add_user_data_tarif_water()

        if(tmp_data_about_water !=self.__number_water_kube):
            self.__number_water_kube = tmp_data_about_water
        if(tmp_data_water_counter != self.__water_counter):
            self.__water_counter = tmp_data_water_counter
        if(tmp_data_number_of_residents !=self.__number_of_residents):
            self.__number_of_residents = tmp_data_number_of_residents
        if(tmp_data_tarif_water != self.__tarif_water):
            self.__tarif_water = tmp_data_tarif_water

            data = []
            data.append(self.__number_water_kube)
            data.append(self.__water_counter)
            data.append(self.__number_of_residents)
            data.append(self.__tarif_water)
        return data


    def return_data_of_water(self):

        return self.__check_water()

a = collection_of_user_data_about_water()
print(a.return_data_of_water())















