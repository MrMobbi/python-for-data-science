

ft_list = ["Hello", "tata"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tutu"}
ft_dict = {"Hello" : "titi"}

ft_list[1] = 'World!'
x = list(ft_tuple)
x[1] = 'Suisse!'
ft_tuple = tuple(x)
ft_set.remove("tutu")
ft_set.add('Lausanne')
ft_dict['Hello'] = '42 Lausanne'


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
