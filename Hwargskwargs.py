from pprint import pprint
contacts = []


class Contact:

    def __init__(self, contact_name, first_name, last_name, phone_number, favorites=False, *args, **kwargs):
        self.contact_name = contact_name
        self.args_tuple = args
        self.kwargs_dict = kwargs
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorites = favorites

    def __str__(self):
        contact = {}
        contact['Контакт'] = self.contact_name
        contact['Имя'] = self.first_name
        contact['Фамилия'] = self.last_name
        contact['Телефон'] = self.phone_number
        if self.favorites:
            contact['В избранных'] = self.favorites
        if self.kwargs_dict:
            contact['Дополнительная информация:'] = {}
            for key, value in self.kwargs_dict.items():
                contact['Дополнительная информация:'][key] = value
        contacts.append(contact)
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

    def __init__(self, title, contact_name, first_name, last_name, phone_number, favorites=False, *args, **kwargs):
        super().__init__(contact_name, first_name, last_name, phone_number, favorites, *args, **kwargs)
        self.title = title

    def delete_contact(self, phone_number):
        for contact in contacts:
            if contact['Телефон'] == phone_number:
                del contact['Контакт']
                print('Контакт удален')

    def get_favorites(self):
        return self.favorites

    def get_contact_by_name(self, first_name, last_name):
        for contact in contacts:
            if first_name in contact['Имя'] and last_name in contact['Фамилия']:
                yield contact['Контакт']


jhon = PhoneBook('jhon', 'Контакты', 'Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
jhon.__str__()
