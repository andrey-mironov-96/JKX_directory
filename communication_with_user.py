print()
from General_data_user import General_data_user as general

import  time
from random import randrange as rand

print("Запуск приложения")
tat = 0

while tat<=100:
    print(tat,"%")
    tat +=rand(11,23)
    time.sleep(0.5)
else:
    print("100 %")
    print("Приложение успешно запущено ...")
general_data = general().return_user_data()


is_water_cold = str(input("1 - в жилье установдлен счетчик холодной воды\n"
                      "0 - в жилье не устанавлен счетчик холодной воды\n: "))

if(is_water_cold == "1"):
    print("Есть счетчик")
elif(is_water_cold == "0"):
    print("Нет счетчика")
else:
    print("Некорректные данные")






