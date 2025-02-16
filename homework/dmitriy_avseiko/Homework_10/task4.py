PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split()
list1 = [x for x in my_list if my_list.index(x) % 2 == 0]
list2 = [int(x[:-1]) for x in my_list if my_list.index(x) % 2 != 0]
price_dict = dict(zip(list1, list2))
print(price_dict)
