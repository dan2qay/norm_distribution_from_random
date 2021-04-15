from random import randint
import matplotlib.pyplot as plt

def D(arr): #Высчитывание Дисперсии
    Disp = 0
    mid = sum(arr)/len(arr)
    for n in arr:
        Disp += (n - mid) ** 2
    Disp /= len(arr)
    return Disp

def sigma(arg):
    if str(type(arg)) == "<class 'int'>":
        return arg ** 1/2
    else:
        return D(arg) ** 1/2

def choiselist(arr, count):  # Выборка неповторяющихся элементов. Если есть идеи для оптимизации - welcome.
    arr1 = []
    l = list(range(len(arr)))
    for i in range(count):
        l_l = len(l) - 1
        arr1.append(arr[l.pop(randint(0, l_l))])
    return arr1


heights = [randint(150, 190) for i in range(100)]  # Рандомно заполним список длинами ростов учеников класса N

'''
Теперь сформируем 50 выборок по 30 человек
из генерального списка учеников. Посмотрим на график средних значений, оценим, нормально ли распределен
новый список или нет. Для отображения графика будет использоваться tkinter.
'''

selections = []
averages = []

for i in range(50):  # Количество выборок
    selections.append(choiselist(heights, 30))  # Мощность выборок
    averages.append(sum(selections[i]) / len(selections[i]))

# for i in range(len(selections)):
#    print(selections[i], ' : ', averages[i], ' - срзнач')

for i in range(len(selections)):
    print(averages[i], f'срзнач {i + 1}')

print(f'{min(averages)} - минимум из средних, {max(averages)} - максимум')

'''
Возьмем округленное вниз значение средних за минимум, округленное вверх
максимальное - за максимум. С шагом 1 рассмотрим количество средних значений ростов
и построим на этих данных график
'''

min_av = int(min(averages))
max_av = int(max(averages)) + 1
mid_av = sum(averages) / len(averages)
count_of_av = [0 for i in range(min_av, max_av)]

for i in range(len(averages)):
    count_of_av[(int(averages[i])) - min_av] += 1

print(count_of_av)

# Сформируем новый список, который будет отвечать за Y - ординату. Это частота появления определенного
# типа среднего роста в нашем исследовании
Y = []
X = averages

for i in range(len(X)):
    Y.append(count_of_av[int(averages[i]) - min_av])




plt.axvline(x=(mid_av - sigma(averages)), color='r')
plt.axvline(x=(mid_av + sigma(averages)), color='r')
plt.bar(X, Y)
plt.show()
