class Flower:

    def __init__(self, name, price, lifetime, age, color, length):
        self.name = name
        self.price = price
        self.lifetime = lifetime
        self.age = age
        self.color = color
        self.length = length


class Rose(Flower):

    def __init__(self, name, price, lifetime, age, color, length, smell):
        super().__init__(name, price, lifetime, age, color, length)
        self.smell = smell


class Tulip(Flower):

    def __init__(self, name, price, lifetime, age, color, length, is_early):
        super().__init__(name, price, lifetime, age, color, length)
        self.is_early = is_early


class Chamomile(Flower):

    def __init__(self, name, price, lifetime, age, color, length, is_medicinal):
        super().__init__(name, price, lifetime, age, color, length)
        self.is_medicinal = is_medicinal


flower1 = Rose('rose',15, 7, 1, 'red', 50, 'honey')
flower2 = Tulip('tulip',11, 10, 3, 'yellow', 30, True)
flower3 = Chamomile('chamomile',20, 5, 2, 'white', 20, False)

class Bouquet:

    def __init__(self, *args):
        self.flower_list = list(args)
        self.bouquet_price = self.calc_bouquet_price()
        self.bouquet_lifetime = self.calc_bouquet_lifetime()


    def calc_bouquet_price(self):
        bouquet_price = 0
        for i in self.flower_list:
            bouquet_price = bouquet_price + i.price
        return bouquet_price


    def calc_bouquet_lifetime(self):
        lifetime_list = [i.lifetime for i in self.flower_list]
        bouquet_lifetime = sum(lifetime_list) / len(lifetime_list)
        return bouquet_lifetime


    def sort_by_parametr(self, parametr):
        if parametr not in ['name', 'price', 'lifetime', 'age', 'color', 'length']:
            return 'Invalid parametr'
        flower_dict = {i.name: getattr(i, parametr, None) for i in self.flower_list}
        lst_tuples = []
        for item  in flower_dict.items():
            lst_tuples.append(item)
        sort_lst_tuples = sorted(lst_tuples, key = lambda x: x[1])
        sort_by_param_lst = [i[0] for i in sort_lst_tuples]
        return ', '.join(sort_by_param_lst)


    def find_param_value(self, param, param_value):
        param_dict = {i.name: getattr(i, param, None) for i in self.flower_list}
        ans = [i for i in param_dict if param_dict[i] == param_value]
        return ', '.join(ans)


my_bouquet = Bouquet(flower1, flower2, flower3)
print(my_bouquet.bouquet_price)
print(my_bouquet.bouquet_lifetime)
print(my_bouquet.sort_by_parametr('price'))
print(my_bouquet.find_param_value('color', 'yellow'))
