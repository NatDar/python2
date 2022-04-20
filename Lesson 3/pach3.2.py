name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Darovskaya', name = 'Natallia', year = '1982', city = 'Zhlobin', email = 'nat@mail.ru', telephone = '8-375-300-99-87')) 

