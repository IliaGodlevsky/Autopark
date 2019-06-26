# Autopark
Создайте класс который производит легковые автомобили – они будут нам нужны для
класса «таксопарк».
Стоимость литра бензина 2,4$, дизеля – 1,8$.
Создайте 100 машин, из которых класс сам будет выпускать каждый третий автомобиль
дизельным (остальные, соответственно, бензиновые), стандартный бензобак будет 60
литров, а каждый пятый авто – с баком на 75 литров.
Стоимость каждой машины будет 10.000$. Каждая машина должна иметь тахограф (он
считает пройденный километраж), который нельзя сбрасывать/уменьшать.
Максимальный пробег до капремонта бензиновой – 100.000 километров, дизельной –
150.000 км. Пробег без капремонта не может быть превышен – при попытке это сделать
машина должна быть сначала отозвана в СТО и проведен капремонт. Его стоимость для
бензиновой машины 500$, для дизельной – 700$.
Расход топлива у бензиновой – 8 л/100 км, расход дизеля – 6 л/100 км.
Каждая 1.000 км пробега снижает стоимость бензиновой машины на 9.5$, дизельной – на
10.5$, при этом увеличивая расход топлива на 1%.
Создайте уникальный маршрут случайной длины для каждой машины (от 55.000 до
286.000 км), требуя заправлять полный бак авто каждый раз, как он опустеет.
Машины должны уметь предоставлять сведения о себе:
- пробег
- остаточная стоимость
- сколько было потрачено на топливо за всю поездку
- сколько раз машина заправлялась
- сколько осталось пробега до утилизации
После пробега отсортируйте машины: дизельные – по остаточной стоимости, бензиновые
– по тому сколько им осталось ездить.
Посчитайте суммарную стоимость машин а автопарке после пробега.
