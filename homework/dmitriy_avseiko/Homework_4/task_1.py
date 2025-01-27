my_dict = {}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [6, 7, 8, 9, 10]
my_dict['dict'] = {"key1": "11", "key2": "12", "key3": "13", "key4": "14", "key5": "15"}
my_dict['set'] = {16, 17, 18, 19, 20}

print(my_dict['tuple'][-1])
my_dict['list'].append(21)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'value6'
my_dict['dict'].pop('key1')
my_dict['set'].add(22)
my_dict['set'].remove(16)
print(my_dict)
