class JKX(object):

    def __init__(self):
        #Улуги ЖКХ#

        self.__elelectricties = 1 #Электроэнергия
        self.__plumbing = 1  #Переменная воды
        self.__theRemunerationOfTheChairMan = 1 #Вознаграждение председателя дома
        self.__gas = 1 # Цена за куб газа //
        self.__doorPhone = 1 #Домофон
        self.__TV = 1 #Телевидение
        self.__repair = 1 #Капитальный ремонт
        self.__heating = 1 #Отопление
        self.__repairHome = 1 #Ремонт дома
        self.__housingMaintenance = 1 #Содержание жилья (Дворники, скамейки)
        self.__cleaning = 1 #Уборка
        self.__coldPlumbing = 1 #Холодная вода(Коэффициент)
        self.__coldPlumbing = 1 #Холодная вода
        self.__elelectrictiesAllHome = 1 #Электричество общего дома
        #Сведения о жилье
        self.__areaHome = 1 #Площадь жилья(квартира, дом)

        #Тарифы
        self.__repairHomeTarif = 1 #ремонт жилья
        self.__upkeepHomeTarif = 1 #содержание жилья
        self._kapital_repair_home = 1 #Капитальный ремот дома

        self.__plumbingTarif = 1 #Тариф на воду
        self.__gasTarif = 1 #Тариф на газ
        self.__heatingTarif = 1 #Тариф на отопление
        self.__coldPlumbingTarif = 1 #Тариф на холодную воду
        self.__elelectrictiesTarif = 1 #Тариф на электроэнергию
        self.__coldPlumbingAllHomeTarif = 1 #Тариф на воду общедомовых нужд

        self.__recalculation = 0 #Перарасчет
        self.__facilities = 0 #Льготы
        self.__residue = 0 #остаток

        #ИТОГО
        self.__subtotal = 0 #Итого за ЖКХ

    def __CalculationRepairHome(self):
        """Расчет услуги ремонт жилья
       x = тариф * площадь + перерасчет - льготы + остаток
        Возвращает стоимость услуги в переменную __repairHome
        """

        self.__repairHome = (self.__repairHomeTarif*self.__areaHome + self.__recalculation
                             - self.__facilities + self.__residue)
        pass

    def CheckCalculationRepairHome(self,repairHomeTarif:float,areaHome:float,
                                   recalculation= 0,facilities = 0,residue = 0):
        """Функция принимает данные и передает их в приватные переменные,
        а после вызывает функцию подсчета ремонта жилья
        Входные данные: тариф на ремонт жилья, площадь жилья,
        перерасчет(по умолчанию 0), льготы(по умолчанию 0),остаток (по умолчанию 0)
        """
        self.__areaHome = areaHome
        self.__repairHomeTarif = repairHomeTarif
        self.__recalculation = recalculation
        self.__facilities = facilities
        self.__residue = residue
        self.__CalculationRepairHome()
        pass

    def CheckCalculationUpkeepHome(self,upkeepHomeTarif:float,areaHome:float,
                                   recalculation = 0, facilities = 0,residue = 0):
        """Функция принимает данные и передает их в приватные переменные,
        а после вызывает функцию подсчета содержания жилья
        Входные данные: тариф на ремонт жилья, площадь жилья,
        перерасчет(по умолчанию 0), льготы(по умолчанию 0),остаток (по умолчанию 0)
                """
        self.__upkeepHomeTarif = upkeepHomeTarif
        self.__areaHome = areaHome
        self.__recalculation = recalculation
        self.__facilities = facilities
        self.__residue = residue
        self.__CalculationUpkeepHome()
    def __CalculationUpkeepHome(self):
        """Расчет услуги содержание жилья
               x = тариф * площадь + перерасчет - льготы + остаток
              Возвращает стоимость услуги в переменную __housingMaintenance
              """
        self.__housingMaintenance = (self.__upkeepHomeTarif * self.__areaHome + self.__recalculation -
                                     self.__facilities + self.__residue)
        pass

    def check_calculation_repair_all_home(self,repair_all_home_tarif:float,area_home:float,
                                          recalculation = 0,facilities = 0,residue = 0):

        """Функция принимает данные и передает их в приватные переменные, а после вызывает функцию подсчета содержания жилья
                       Входные данные: тариф на капитальный ремонт дома, площадь жилья, перерасчет(по умолчанию 0),
                       льготы(по умолчанию 0),остаток (по умолчанию 0)
                       """
        self._kapital_repair_home = repair_all_home_tarif
        self.__areaHome = area_home
        self.__recalculation = recalculation
        self.__facilities = facilities
        self.__residue = residue
        self.__calculation_repair_all_home()




    def __calculation_repair_all_home(self):
        """Расчет услуги капитальный ремонт дома
                      x = тариф * площадь + перерасчет - льготы + остаток
                     Возвращает стоимость услуги в переменную __repair
                     """
        self._kapital_repair_home = (self._kapital_repair_home * self.__areaHome + self.__recalculation - self.__facilities +
                                     self.__residue)

    def __calculation_plumbing(self):
        """Функция производит расчет водоотведения
        по формуле = (тариф * (количество воды по счетчику, либо по количесту кубов на человека) +
        перерасчет - льготы + остаток )
        возвращает результат _plumbing
        """
        pass


    def testPrint(self):
        print(self._kapital_repair_home)
        pass

a = JKX()




















