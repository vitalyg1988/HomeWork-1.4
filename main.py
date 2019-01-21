import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

header = flats_list.pop(0)
#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


#TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
print("TASK 1:")
print(' ')
num_id = []
for flat in flats_list:
  if flat[2] == "новостройка":
    num_id.append(flat[0])
    print("Квартира новостройка: {} ".format(flat))
print(' ')
print("Количество новостроек: ", len(num_id))
print(' ')
print("Список id-новостроек: ", num_id)

# 2) добавьте в код подсчет количества новостроек


#TODO 2:
# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
print(' ')
print("TASK 2:")
print(' ')
flat_info = {}
for flat in flats_list:
  flat_info = {"ID":flat[0], "Количество комнат":flat[1], "Новостройка/вторичка":flat[2], "Цена(руб.)":flat[11]}
  print(flat_info)
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1
print(' ')
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  # if subway not in subway_dict.keys():
  #   subway_dict[subway] = list()
  subway_dict.setdefault(subway, list())
  subway_dict[subway].append({flat[12]})

print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
print(' ')
for subway, flat_info in subway_dict.items():
  print('Метро {0} количество квартир: {1}'.format(subway, len(flat_info)))