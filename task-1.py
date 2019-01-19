"""
Задача №1. Понимание типов данных.
"""

contact_dict = {
                'Список контактов':
               [
                 {
                'name': 'Олег Смирнов',
                'mobile_phone': '+7-994-387-12-45',
                'age': 28,
                'profession': 'водитель',
                'organization': 'Нетология'},
               {
                'name': 'Денис Иванов',
                'mobile_phone': '+7-910-234-54-82',
                'age': 23,
                'profession': 'тренер по йоге',
                'organization': 'Фитнес Клуб'},
               {
                'name': 'Андрей Потапов',
                'mobile_phone': '+7-905-117-53-00',
                'age': 36,
                'profession': 'менеджер',
                'organization': 'Нетология'},
               {
                 'name': 'Илья Казаков',
                 'mobile_phone': '+7-928-345-89-65',
                 'age': 42,
                 'profession': 'повар',
                 'organization': 'Ресторан'},
               {
                 'name': 'Захар Лебедев',
                 'mobile_phone': '+7-911-357-89-12',
                 'age': 25,
                 'profession': 'промоутер',
                 'organization': 'Нетология'},
               {
                 'name': 'Юлия Гранц',
                 'mobile_phone': '+7-998-741-22-11',
                 'age': 31,
                 'profession': 'стилист',
                 'organization': 'Салон Красоты'},
               {
                 'name': 'Глеб Жуков',
                 'mobile_phone': '+7-932-358-77-41',
                 'age': 38,
                 'profession': 'ювелир',
                 'organization': 'ЮЗ SOKOLOV'},
               {
                 'name': 'Сергей Фрост',
                 'mobile_phone': '+7-912-452-45-66',
                 'age': 22,
                 'profession': 'каскадёр',
                 'organization': 'Мосфильм'},
               {
                 'name': 'Ольга Лунёва',
                 'mobile_phone': '+7-952-112-51-06',
                 'age': 39,
                 'profession': 'стоматолог',
                 'organization': 'Клиника Зубик'},
               ]
                 }

def search_contact_number(obj, organization= 'Нетология'):
  print('Список контактов: ')
  for contact in obj['Список контактов']:
    print("{0} {1} ".format(contact.get('name'), contact.get('mobile_phone')))
  print(' ')
  netology_list = []
  other_list = []
  for contact in obj['Список контактов']:
    if contact['organization'] == organization:
      netology_list.append(contact['name'])
      num_of_employees = len(netology_list)
    else:
      other_list.append(contact['name'])
  print('Список людей, работающих в Нетологии количестве {} человек: '.format(num_of_employees))
  print(*netology_list, sep=', ')
  netology_set = set(netology_list)
  other_set = set(other_list)
  difference_set = other_set.difference(netology_set)
  print(' ')
  print('Спикок людей не работающих в Нетологии:', *difference_set, sep=', ')

search_contact_number(contact_dict)