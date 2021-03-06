from random import randint
import matplotlib.pyplot as plt


def D(arr):  # Высчитывание Дисперсии
    Disp = 0
    mid = sum(arr) / len(arr)
    for n in arr:
        Disp += (n - mid) ** 2
    Disp /= len(arr)
    return Disp


def sigma(arg):
    if str(type(arg)) == "<class 'int'>":
        return arg ** 1 / 2
    else:
        return D(arg) ** 1 / 2


def choiselist(arr, count):  # Выборка неповторяющихся элементов. Если есть идеи для оптимизации - welcome.
    arr1 = []
    l = list(range(len(arr)))
    for i in range(count):
        l_l = len(l) - 1
        arr1.append(arr[l.pop(randint(0, l_l))])
    return arr1


heights = [randint(140, 200) for i in range(
    int(input('Сколько учеников участвует в опросе? ')))]  # Рандомно заполним список длинами ростов учеников класса N

'''
Теперь сформируем выборки
из генерального списка учеников. Посмотрим на график средних значений, оценим, нормально ли распределен
новый список или нет. Для отображения графика будет использоваться tkinter.
'''

selections = []
averages = []
count_of_samples = int(input('Введите количество выборок: '))
sample_size = int(input('Сколько учеников в каждой выборке? '))

for i in range(count_of_samples):  # Количество выборок
    selections.append(choiselist(heights, sample_size))  # Мощность выборок
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
# X = averages
X = sorted(averages)

for i in range(len(X)):
    Y.append(count_of_av[int(X[i]) - min_av])

plt.axvline(x=(mid_av - sigma(averages)), color='g')
plt.text(mid_av - sigma(averages), 0.5, 'sigma', rotation=90)
plt.axvline(x=(mid_av + sigma(averages)), color='g')
plt.text(mid_av + sigma(averages), 0.5, 'sigma', rotation=90)
plt.bar(X, Y)
plt.plot(X, Y, 'r', marker=11)
plt.show()
