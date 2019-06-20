class Contact:

    def __init__(self, first_name, last_name, phone_number, favorites=False, *args, **kwargs):
        self.args_tuple = args
        self.kwargs_dict = kwargs
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorites = favorites

    def __str__(self):
        print(f'Имя: {self.first_name}')
        print(f'Фамилия: {self.last_name}')
        print(f'Телефон: {self.phone_number}')
        if self.favorites == False:
            print(f'В избранных: нет')
        else:
            print(f'В избранных: {self.favorites}')
        if self.kwargs_dict:
            print('Дополнительная информация:')
            for key, value in self.kwargs_dict.items():
                print(f'        {key} : {value}')


class PhoneBook(Contact):

    def __init__(self, title, first_name, last_name, phone_number, favorites=False, *args, **kwargs):
        super().__init__(first_name, last_name, phone_number, favorites, *args, **kwargs)
        self.title = title

    def __del__(self, phone_number):
        del self
        print('Контакт удален')

    def get_contact(self):
        return self.__str__()

    def get_favorites(self, favorites):
        return list(favorites)

    def get_contact_by_name(self, first_name, last_name):
        return self.__str__()


jhon = PhoneBook('Контакты', 'Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
